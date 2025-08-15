import streamlit as st
from SHORTS import SHORTS
from Rolls import Rolls
from Char import Char
from tables import dev_points, Bonus
from utils.files import get_files_in_dir
from utils.ui_elements import show_assignment_explanation, show_character_inputs, do_dialog
from utils.save_char import save_char
from utils.auswahl_ui import show_selection_summary
#import importlib

roller = Rolls(100, minimum=20)

st.session_state["go_to_test"] = False  # Flag für Seitenwechsel setzen

job_classes = get_files_in_dir("jobs")
races = get_files_in_dir("races")
age_range = list(range(16, 999))
age_range.append(0000)

# Dropdowns und Eingabefelder anzeigen
selected_name, selected_more_name, selected_job, selected_race, selected_age = show_character_inputs(job_classes, races, age_range)

bob = Char("Bob", 19, job=selected_job, race=selected_race)

# Erklärung/Expander anzeigen
show_assignment_explanation()

def do_max(collection):
    print("do_max")
    #for c in collection:
        #print(f"is: {c}")
    
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

avg = sum(row_labels)/len(row_labels)
st.write(f"**Durchschnitt der 10 Würfelwerte:** {avg} ({avg-60:.1f}) -- *vor der Verteilung der Werte*")

# Kopfzeile der Tabelle anzeigen
header_cols = st.columns(len(columns) + 1)  # +1 für die Zeilenbeschriftung
header_cols[0].write("**Würfe**")  # Erste Spalte für Zeilenbeschriftungen
job_markings = bob.job.prime_stats
dev_markings = ["CO", "AG", "SD", "ME", "RE"]

# Tabelle mit Checkboxen anzeigen
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
#            break
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
        save_char(bob,
                  selected_per_row.items(),
                  job_markings,
                  selected_age,
                  selected_race,
                  selected_more_name,
                  avg,
                  selected_job
        )

# "Übernehmen"-Button NUR anzeigen, wenn gespeichert wurde
if st.session_state.get("saved", False) and selected_count == 10:
    if st.button("Übernehmen"):
        if selected_name == "":
            do_dialog("your name", "farts")

        save_char(bob, selected_per_row.items(), job_markings, selected_age, selected_race, selected_more_name, avg, selected_job)
        
        
        st.session_state["bob"] = bob
        st.session_state["go_to_test"] = True  # Flag für Seitenwechsel setzen

# Seitenwechsel am Ende der Seite prüfen (damit nicht im Button-Callback!)
if st.session_state.get("go_to_test", False):
    # Hiermit wird bei Streamlit >=1.22.0 die Seite gewechselt
    st.switch_page("pages/test.py") 


# Zeige die Auswahl und die Auswirkungen der Auswahl oben
show_selection_summary(selected_count, selected_per_row, SHORTS, dev_markings, dev_points, Bonus, job_markings)

import streamlit as st

def show_character_inputs(job_classes, races, age_range):
    col1, col2, col3 = st.columns(3)
    selected_name = col1.text_input("Gib einen Namen ein", help="the name please")
    selected_more_name = col2.text_input("Gib einen Namenszusatz ein")
    col1, col2, col3 = st.columns(3)
    selected_job = col1.selectbox("Wähle Deine Klasse", job_classes, index=3)
    selected_race = col2.selectbox("Wähle Dein Volk", races, index=1, help="Hilfe zu den einzelnen Völkern gibt es nur für das jeweils ausgewählte.")
    age_help = "Alter eingeben oder auswählen.\nWenn größer 999, dann kann man die Option 'andere...' wählen."
    selected_age = col3.selectbox("Wähle Deine Alter", age_range, index=2, help=age_help)
    return selected_name, selected_more_name, selected_job, selected_race, selected_age

def show_assignment_explanation():
    st.subheader("Zuweisung der Werte zu Eigenschaften", divider="red")
    with st.expander("wenn eine Erklärung gebraucht wird:"):
        st.write("Für Deinen Charakter wurde bereits 10x gewürfelt.")
        st.write("Die Ergebnisse befinden sich in der linken Spalte (unter **Würfe**).")
        st.write("Du kannst diese Werte den Eigenschaften zuweisen, indem Du die Kreuzchen setzt.")
        st.write("-- Jeder nur ein Kreuz! -- dafür sorgt das Programm selbst --")
        st.text("Sobald Du einen Wert ausgewählt hast, werden die Auswirkungen Deiner Auswahl unten kommentiert.")
        st.write("- Werte mit einem Sternchen (&#9734;) sind für die Berechnung der Entwicklungspunkte verantwortlich, **für alle Klassen gleichermaßen.**")
        st.write("- Werte mit einem Pfeil nach oben (&#x2B06;) werden auf 90 angehoben, weil sie die Haupteigenschaften Deines Charakters und der gewählten Charakterklasse sind. Je nach Auswahl der Charakterklasse ändern sich auch die Haupteigenschaften.")
        st.warning("Erst wenn **alle 10 Werte** verteilt wurden, kannst Du die Verteilung speichern und für den Charakter übernehmen.") 
        st.write("- Welcher Wert noch fehlt, sieht man leicht in der Auswahlbeschreibung unter dem Feld.")
        st.error("Beachte, sind die Anfangswerte Deines Charakters. In einem nächsten Schritt wird für jeden Wert erneut gewürfelt, um den potentiellen Maximalwert zu ermitteln, den Dein Charakter im Laufe seiner Karriere erreichen kann, wenn er lang genug überlebt.")

def do_dialog(long_str: str, short_str: str):
    """
    Display a dialog indicating a missing input.
    """
    st.dialog("You forgot: ")
    st.write(f"{long_str} ({short_str})")
    if st.button("got it!"):
        st.rerun()
