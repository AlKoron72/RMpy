import streamlit as st
import pandas as pd
from Char import Char
from SHORTS import SHORTS
import time

if "show_info" not in st.session_state:
    st.session_state["show_info"] = False
if "info_time" not in st.session_state:
    st.session_state["info_time"] = 0

# Funktion, um die Statistiken eines Char-Objekts in einen DataFrame zu konvertieren
def char_stats_to_dataframe(char_obj):
    data = {
        "Name": [],
        "Value": [],
        "MAX": [],
        "Bonus": [],
        "Bonus-Race": [],
        "Total Bonus": [],
    }
    for stat in char_obj.Stats:
        data["Name"].append(SHORTS[stat.name].value)
        data["Value"].append(stat.value)
        data["MAX"].append(stat.max_value)
        data["Bonus"].append(stat.bonus)
        data["Bonus-Race"].append(stat.bonus_race)
        data["Total Bonus"].append(stat.total)
    return pd.DataFrame(data)

def get_job_classes(directory="jobs"):
    # Listet alle .py-Dateien im Verzeichnis auf, ohne die Endung .py
    return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]


# Prüfe, ob Bob übergeben wurde
if "bob" in st.session_state:
    bob = st.session_state["bob"]
    #print(bob.get)
    
    if st.button("Zeige Info-Box für 3 Sekunden"):
        st.session_state["show_info"] = True
        st.session_state["info_time"] = time.time()

    if st.session_state["show_info"]:
        st.info("Dies ist eine temporäre Info-Box.")
        if time.time() - st.session_state["info_time"] > 3:
            st.session_state["show_info"] = False
            st.rerun()
        
    if st.button("Zeige Info-Box"):
        st.info("Streamlit-Version: " + st.__version__)

    
    if st.button("Zeige Expander"):
        with st.expander("Mehr Infos anzeigen"):
            st.write("Hier stehen zusätzliche Details.")

    st.write("Bob wurde übergeben:")
    st.text(f"Name:{bob.name:>23}")
    st.text(f"Alter:{bob.age:>25}")
    st.text(f"Beruf:{bob.job.name:>31}")
    st.text(f"{bob.Stats[-1].name}:{bob.Stats[-1].max_value:>31}")

    #st.write(str(bob))

    # Konvertiere die Statistiken in einen DataFrame
    df = char_stats_to_dataframe(bob)

    # Streamlit-Anwendung
    st.title("Charakterstatistiken:")
    st.write("Dies ist eine Tabelle mit den Statistiken des Charakters.")

    # Zeige den DataFrame in Streamlit an
    st.dataframe(df.set_index("Name"))

    if st.button("Roll Max"):
        #st.write(bob.Stats[0])
        for stat in bob.Stats:
            stat.set_max_value(0)
#            stat.max_value = stat.set_max_value(stat.value)
            st.write(f"{stat.name}: {stat.value} / {stat.max_value}")
else:
    st.write("Kein Charakter übergeben.")