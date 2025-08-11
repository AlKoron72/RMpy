import os
import streamlit as st
from SHORTS import SHORTS
from Rolls import Rolls
from Char import Char

roller = Rolls(100, minimum=20)

st.session_state["go_to_test"] = False  # Flag für Seitenwechsel setzen


def get_job_classes(directory="jobs"):
    # Listet alle py-Dateien im Verzeichnis auf, ohne die Endung .py
    return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]

def get_races(directory="races"):
    # Listet alle py-Dateien im Verzeichnis auf, ohne die Endung .py
    return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]

job_classes = get_job_classes()
races = get_races()
age_range = list(range(16, 999))
age_range.append(0000)

# Spalten anlegen
col1, col2, col3 = st.columns(3)

# Dropdown-Menus from folder jobs/races content
# char-names and misc data collection
selected_name = col1.text_input("Gib einen Namen ein", help="you name dummy")
selected_more_name = col2.text_input("Gib einen Namenszusatz ein")
#st.divider()
#----
col1, col2, col3 = st.columns(3)
selected_job = col1.selectbox("Wähle Deine Klasse", job_classes, index=3)
selected_race = col2.selectbox("Wähle Dein Volk", races, index=1)
age_help = "Alter eingeben oder auswählen.\nWenn größer 999, dann kann man die Option 'andere...' wählen."
selected_age = col3.selectbox("Wähle Deine Alter", age_range, index=2, help=age_help)

bob = Char("Bob", 19, job=selected_job, race=selected_race)

# Spaltennamen aus dem Enum extrahieren
columns = [short.name for short in SHORTS]
row_labels = []

# Benutzerdefinierte Zeilenbeschriftung
if "row_labels" not in st.session_state:
    st.session_state.row_labels = []
    for s in SHORTS:
        numb = int(roller.roll())
        st.session_state.row_labels.append(numb)
    st.session_state.row_labels.sort()
row_labels = st.session_state.row_labels

def do_max(collection):
    print("do_max")
    #for c in collection:
        #print(f"is: {c}")
    
# save Button-Function
def do_save(selected_items, job_stats):
    st.write("folgende Werte gespeicherter:")
    my_collection = []
    
    for column_name, row_label in selected_items:
        if row_label:
            if column_name in job_stats:
                # for job stats
                my_collection.append(f"{column_name}: {max(90, row_label)}")
                bob.set_stat_value(column_name, max(90, row_label))
            else:
                # all the non-job-stats
                my_collection.append(f"{column_name}: {row_label}")
                bob.set_stat_value(column_name, row_label)
        else:
            my_collection.append(f"{column_name}: Keine Auswahl")
            
    mySum = 0
    for s in bob.Stats:
        mySum += s.value

    bob.age = selected_age
    bob.race = selected_race

    st.write(f"{str(my_collection)}")
    st.write(f"neuer Durchschnitt: {mySum/10}")
    # saving bob in session 
    st.session_state["saved"] = True  # <-- Save-FLAG setzen
    st.session_state["bob"] = bob     # <-- Bob in den session_state speichern


# Funktion, um den Zustand zu prüfen und nur eine Checkbox pro Zeile/Spalte zuzulassen
def enforce_single_selection(row_idx, col_idx):
    # Schlüssel der aktuell geklickten Checkbox
    current_key = f"{row_idx}_{col_idx}"
    
    # Überprüfen, ob Checkbox aktiviert wurde
    if st.session_state[current_key]:
        # Deaktiviere alle anderen Checkboxen in derselben Zeile
        for c in range(len(columns)):
            if c != col_idx:
                st.session_state[f"{row_idx}_{c}"] = False
        
        # Deaktiviere alle anderen Checkboxen in derselben Spalte
        for r in range(len(row_labels)):
            if r != row_idx:
                st.session_state[f"{r}_{col_idx}"] = False


# Tabelle mit Checkboxen anzeigen
st.header("Kreuz-Tabelle")
#st.write("Zeilenbeschriftungen (row_labels):", row_labels)
avg = sum(row_labels)/len(row_labels)
st.write(f"Durchschnitt: {avg} ({avg-60:.1f})")

# Kopfzeile der Tabelle anzeigen
header_cols = st.columns(len(columns) + 1)  # +1 für die Zeilenbeschriftung
header_cols[0].write("Würfe")  # Erste Spalte für Zeilenbeschriftungen
job_markings = bob.job.prime_stats
dev_markings = ["CO", "AG", "SD", "ME", "RE"]

for col, column_name in zip(header_cols[1:], columns):
    if column_name in job_markings and column_name in dev_markings:  
        # Dev-Stat UND Job-Stat
        col.markdown(
            f'<span style="color:#0000cc; font-weight:bold;">{column_name} &#x2B06; </span>&#9734;',
            unsafe_allow_html=True,
        )
    elif column_name in dev_markings:  
        # Dev-Stat
        col.markdown(
            f'<span style="color:#0000cc; font-weight:bold;">{column_name} </span>&#9734;',
            unsafe_allow_html=True,
        )
    elif column_name in job_markings:  
        # Job-Stat
        col.markdown(
            f'<span style="color:#00cc00; font-weight:bold;">{column_name} &#x2B06;</span>',
            unsafe_allow_html=True,
        )
    else:
        col.write(column_name)  # Normale Spaltennamen

# Tabelle erstellen
for row_idx, row_label in enumerate(row_labels):  # `row_labels` werden für Zeilen verwendet
    row_cols = st.columns(len(columns) + 1)  # +1 für die Zeilenbeschriftung
    row_cols[0].write(row_label)  # Erste Spalte zeigt die benutzerdefinierte Zeilenbeschriftung
    for col_idx, (col, column_name) in enumerate(zip(row_cols[1:], columns)):
        # Eindeutigen Schlüssel erstellen
        unique_key = f"{row_idx}_{col_idx}"
        
        # Checkbox erstellen
        with col:
            st.checkbox(
                "",
                key=unique_key,  # Eindeutiger Schlüssel
                on_change=enforce_single_selection,  # Funktion bei Änderung aufrufen
                args=(row_idx, col_idx),  # Argumente für die Funktion
            )

# --- Ergebnis unter der Tabelle anzeigen ---

# Zähle die Anzahl der gesetzten Checkboxen
selected_count = sum(
    st.session_state[f"{row_idx}_{col_idx}"]
    for row_idx in range(len(row_labels))
    for col_idx in range(len(columns))
)

# Pro Zeile herausfinden, welche Checkbox aktiviert ist
selected_per_row = {}
for col_idx, column_name in enumerate(columns):  # Iteriere über alle Spalten
    selected_row = None  # Standardwert, falls keine Auswahl getroffen wurde
    for row_idx, row_label in enumerate(row_labels):  # Iteriere über alle Zeilen
        if st.session_state[f"{row_idx}_{col_idx}"]:
            selected_row = row_label  # Speichere die Zeilenbeschriftung der aktivierten Checkbox
            break
    # Füge die Spalte und den zugehörigen Wert (oder "Keine Auswahl") hinzu
    if selected_row is not None:
        selected_per_row[column_name] = selected_row
    else:
        selected_per_row[column_name] = "    ---"

def set_list(active: bool):
    # Setze erst alle Checkboxen auf False
    for row_idx in range(len(row_labels)):
        for col_idx in range(len(columns)):
            st.session_state[f"{row_idx}_{col_idx}"] = False
    # Setze die Hauptdiagonale auf True
    if active:
        for idx in range(min(len(row_labels), len(columns))):
            st.session_state[f"{idx}_{idx}"] = True
    st.rerun()

st.write(f"**Anzahl der aktivierten Checkboxen:** {selected_count}")

#if st.button("Zufallsverteilung"):
#    st.warning("nichts dem Zufall überlassen")
#    set_list(True)

# Zeige die Anzahl der aktivierten Checkboxen
if selected_count == 10:
    if st.button("Save", key="save"):
        do_save(selected_per_row.items(), job_markings)

# "Übernehmen"-Button NUR anzeigen, wenn gespeichert wurde
if st.session_state.get("saved", False):
    if st.button("Übernehmen"):
        do_save(selected_per_row.items(), job_markings)
        st.session_state["bob"] = bob
        st.session_state["go_to_test"] = True  # Flag für Seitenwechsel setzen

# Seitenwechsel am Ende der Seite prüfen (damit nicht im Button-Callback!)
if st.session_state.get("go_to_test", False):
    # Hiermit wird bei Streamlit >=1.22.0 die Seite gewechselt
    st.switch_page("pages/test.py") 


# Zeige die Auswahl und die Auswirkungen der Auswahl oben
if selected_count > 0:
    st.header("Auswahl:")
    for column_name, row_label in selected_per_row.items():  # Iteriere durch alle Spalten
        try:
            row_label_int = int(row_label)  # Versuch, row_label in eine Ganzzahl umzuwandeln
            if column_name in job_markings and row_label_int < 90:
                st.info(f"{SHORTS[column_name].value}: \t{row_label:<25} wird auf 90 angehoben", icon="🚨")        
            else:
                st.write(f"- {SHORTS[column_name].value}: \t{row_label:<25}")
        except ValueError:
            st.markdown(f"**kein Wert für:** {SHORTS[column_name].name} ({SHORTS[column_name].value})")