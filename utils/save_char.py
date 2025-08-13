import streamlit as st
import Char
from jobs.master import Job
from races.master import Race

def save_char(char: Char, 
                selected_items, 
                job_stats: list[str], 
                selected_age: int, 
                selected_race: Race, 
                selected_more_name: str, 
                avg: float,
                selected_job: Job,
                ):
    """
    Speichert und aktualisiert die Werte eines Char-Objekts.
    """
    st.write("folgende Werte gespeichert:")
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
            
    mySum = sum(s.value for s in char.Stats)

    char.age = selected_age
    char.race = selected_race
    char.more_name = selected_more_name
    char.job = selected_job

    #ST display-elements
    st.write(f"{str(my_collection)}")
    st.write(f"neuer Durchschnitt: {mySum/10} {round(mySum/10-avg, 2):+} besser als vorher")
    
    # ST-Session to be saved
    st.session_state["saved"] = True
    st.session_state["bob"] = char

# Hier kannst du weitere Funktionen wie load_char(), update_char(), delete_char() usw. ergänzen.