import importlib
import streamlit as st
from Char import Char
#from jobs.master import Job
#from races.master import Race

def save_char(
    char: Char,
    selected_items,
    job_stats: list[str],
    selected_age: int,
    selected_race: str,     # wird in ein Race-Objekt konvertiert
    selected_more_name: str,
    avg: float,
    selected_job: str,      # wird unten in ein Job-Objekt konvertiert
):
    """
    Speichert und aktualisiert die Werte eines Char-Objekts.
    Konvertiert den Job-String automatisch in ein Job-Objekt.
    """
    # Konvertiere den Job-String in ein Job-Objekt
    try:
        if selected_job != "Berufsloser":
            job_module = importlib.import_module(f"jobs.{selected_job}")  # Lade das Job-Modul
            job_class = getattr(job_module, selected_job)  # Hole die Job-Klasse
            selected_job = job_class(selected_job)  # Erstelle ein Job-Objekt

    except (ModuleNotFoundError, AttributeError) as e:
        st.error(f"Fehler beim Laden eines Objekts: {e}")
        return

    try:
        # Dynamically load race module
        race_module = importlib.import_module(f"races.{selected_race}")  # Import races.<selected_race>
        race_class = getattr(race_module, selected_race)  # Get class from module
        selected_race = race_class()  # Ensure this matches constructor: likely no arguments
    except (ModuleNotFoundError, AttributeError, TypeError) as e:
        st.error(f"Fehler beim Laden der Rasse '{selected_race}': {e}")
        return

    # Assign race
    char.race = selected_race

    # Aktualisiere den Charakter
    char.job = selected_job.name
    char.age = selected_age
    char.race = selected_race
    char.more_name = selected_more_name

    # Statistiken aktualisieren
    st.write("Folgende Werte gespeichert:")
    my_collection = []
    for column_name, row_label in selected_items:
        if row_label:
            if column_name in job_stats:
                my_collection.append(f"{column_name}: {max(90, row_label)}")
                char.set_stat_value(column_name, max(90, row_label))
            else:
                my_collection.append(f"{column_name}: {row_label}")
                char.set_stat_value(column_name, row_label)
        else:
            my_collection.append(f"{column_name}: Keine Auswahl")

    my_sum = sum(s.value for s in char.Stats)

    # Speichere die Ergebnisse in Streamlit
    st.write(f"{str(my_collection)}")
    st.write(f"Neuer Durchschnitt: {my_sum / 10:.1f} (+{round(my_sum / 10 - avg, 2):.2f} besser als vorher)")
    st.session_state["saved"] = True
    st.session_state["bob"] = char