import streamlit as st
import pandas as pd
from SHORTS import SHORTS
from Rolls import Rolls

# Erzeugt 10 zufällige Werte zwischen 1 und 100
def generate_random_rolls():
    roller = Rolls(100)
    return sorted([roller.roll() for _ in range(10)])

# Erstelle DataFrame mit Checkbox-Logik
def create_table_with_checkboxes(rolls, shorts_names):
    data = {"Rolls": rolls}

    # Initialisiere leere Bool-Arrays für die Checkboxen
    for short in shorts_names:
        data[short] = [False] * len(rolls)

    return pd.DataFrame(data)

# Überprüft die Gültigkeit der Tabelle nach jeder Änderung
def validate_unique_selections(df, shorts_names):
    assigned_rolls = []
    error_message = ""

    # Prüfung auf Einzigartigkeit innerhalb jeder Spalte
    for short in shorts_names:
        column_values = [v for v in df[short] if v]
        if len(column_values) != len(set(column_values)):
            error_message = f"Die Spalte '{short}' enthält doppelte Werte!"
            break
        assigned_rolls.extend(column_values)

    # Prüfung auf Einzigartigkeit über alle Spalten hinweg
    if len(assigned_rolls) != len(set(assigned_rolls)):
        error_message = "Ein Würfelwert wurde mehreren Spalten zugewiesen!"

    return error_message

# Hauptfunktion für die Erstellung und Bearbeitung der Tabelle
def render_table_editor():
    st.title("SHORTS Tabelle mit Checkliste")

    # Hole Enum-Schlüssel
    shorts_names = [short.name for short in SHORTS]

    # Lade oder initialisiere den DataFrame
    if "table_df" not in st.session_state:
        rolls = generate_random_rolls()
        st.session_state.table_df = create_initial_dataframe(rolls, shorts_names)

    # Zeige die Tabelle im Bearbeitungsmodus an
    edited_df = st.data_editor(
        st.session_state.table_df,
        num_rows="fixed",  # Anzahl der Zeilen festgelegt
        use_container_width=True,
        key="table_editor"
    )

    # Prüfe auf Fehler
    error_message = validate_unique_selections(edited_df, shorts_names)
    if error_message:
        st.error(error_message)
    else:
        st.success("Die Auswahl ist gültig!")

    # Änderungen speichern
    st.session_state.table_df = edited_df

    # Wenn speichern gedrückt wird
    if st.button("Speichern"):
        st.session_state["final_table"] = st.session_state.table_df
        st.write("Die finale Tabelle lautet:")
        st.write(st.session_state.final_table)

# Starte die App
if __name__ == "__main__":
    render_table_editor()
