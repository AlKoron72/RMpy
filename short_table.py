import streamlit as st
import pandas as pd
import random
from SHORTS import SHORTS  # Dein Enum für die Spaltenüberschriften
from Rolls import Rolls  # Deine Klasse, um Zufallszahlen zu erzeugen


def generate_random_rolls(n=10):
    """
    Generiert eine Liste aus n zufälligen Zahlen zwischen 1 und 100.
    """
    roller = Rolls(100)
    return sorted([roller.roll() for _ in range(n)])


def create_data_editor_table():
    """
    Erstellt die interaktive Tabelle mit `st.data_editor` und implementiert die Logik zur
    Validierung von Checkboxen.
    """
    st.title("Interaktive Tabelle mit SHORTS und Checkbox-Logik")

    # Spaltennamen aus SHORTS extrahieren
    shorts_names = [short.name for short in SHORTS]

    # Zufallswerte für die Zeilen erstellen
    if "random_rolls" not in st.session_state:
        st.session_state["random_rolls"] = generate_random_rolls()

    # DataFrame erstellen
    data = {"Rolls": st.session_state["random_rolls"]}
    for short in shorts_names:
        # Initialisiere die Checkbox-Spalten mit `False`
        data[short] = [False] * len(st.session_state["random_rolls"])

    # Tabelle im Session-State speichern
    if "table_data" not in st.session_state:
        st.session_state["table_data"] = pd.DataFrame(data)

    # Aktuellen DataFrame kopieren
    table_df = st.session_state["table_data"].copy()

    # Tabelle mit `st.data_editor` anzeigen
    edited_df = st.data_editor(
        table_df,
        num_rows="fixed",  # Keine Zeilenzahländerung zulassen
        use_container_width=True,
        hide_index=True,  # Keine Indexspalte anzeigen
        key="shorts_table_editor"
    )

    # Checkbox-Logik anwenden
    enforce_checkbox_logic(edited_df, shorts_names)

    # Aktualisierten DataFrame zurückspeichern
    st.session_state["table_data"] = edited_df

    # Tabelle und aktuelles Mapping anzeigen
    st.write("Aktuelle Tabelle:")
    st.write(edited_df)

    # Validierungsmeldungen anzeigen
    validation_messages = validate_selections(edited_df)
    if validation_messages:
        for message in validation_messages:
            st.error(message)
    else:
        st.success("Die Tabelle erfüllt alle Anforderungen!")

    # Möglichkeit zur Speicherung der Ergebnisse
    if st.button("Speichern"):
        result = save_results(edited_df, shorts_names)
        st.success("Werte erfolgreich gespeichert!")
        st.json(result)


def enforce_checkbox_logic(df, column_names):
    """
    Konflikte zwischen Checkboxen entfernen. Es darf nur eine aktive Checkbox pro Zeile
    und Spalte geben.
    """
    for row_idx, row in df.iterrows():
        # Prüfe, ob in der Zeile eine Checkbox aktiviert wurde
        selected_columns = [col for col in column_names if row[col]]
        if len(selected_columns) > 1:
            # Mehrere Checkboxen in derselben Zeile? Nur die letzte aktiv lassen
            for col in selected_columns[:-1]:
                df.at[row_idx, col] = False

    for col in column_names:
        # Prüfe, ob in der Spalte mehrere ausgewählt sind
        selected_rows = df.index[df[col]].tolist()
        if len(selected_rows) > 1:
            # Mehrere in einer Spalte? Nur die letzte aktiv lassen
            for row_idx in selected_rows[:-1]:
                df.at[row_idx, col] = False


def validate_selections(df):
    """
    Überprüft die Tabelle auf Validierungsprobleme:
    - Jede Zahl darf nur einer Spalte zugewiesen sein.
    - Jede Spalte darf nur einen Wert enthalten.
    """
    errors = []
    used_rows = set()

    # Überprüfe, ob jede Roll-Zeile nur einer Spalte zugewiesen ist
    for row_idx, row in df.iterrows():
        selected_columns = [col for col in df.columns[1:] if row[col]]
        if len(selected_columns) > 1:
            errors.append(f"Zeile {row_idx + 1}: Eine Zahl darf nur einer Spalte zugewiesen werden.")

    # Überprüfe, ob jede Spalte nur eine Zahl enthält
    for col in df.columns[1:]:
        selected_rows = df.index[df[col]].tolist()
        if len(selected_rows) > 1:
            errors.append(f"Spalte '{col}': Jede Zahl darf nur einmal verwendet werden.")
        for row_idx in selected_rows:
            if row_idx in used_rows:
                errors.append(f"Zeile {row_idx + 1}: Eine Zahl wurde mehrfach zugewiesen.")
            used_rows.add(row_idx)

    return errors


def save_results(df, column_names):
    """
    Speichert die finalen Ergebnisse in einem Dictionary, das die Zuweisungen
    der Spaltennamen zu Werten enthält.
    """
    results = {}
    for col in column_names:
        selected_rows = df.index[df[col]].tolist()
        if selected_rows:
            # Speichere die erste ausgewählte Zeile der Spalte
            results[col] = df.at[selected_rows[0], "Rolls"]
        else:
            results[col] = None
    return results


if __name__ == "__main__":
    create_data_editor_table()