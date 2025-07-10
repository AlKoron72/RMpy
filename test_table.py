import streamlit as st
import pandas as pd
from Char import Char
from SHORTS import SHORTS
import os

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

job_classes = get_job_classes()

# Dropdown-Menu from folder jobs content
selected_job = st.selectbox("Wähle eine Klasse:", job_classes)

# Erstelle ein Beispiel-Charakter-Objekt
char = Char(name="Bob Mustermann", age=30, job=selected_job, random_set=True)

# Fülle die Statistiken zufällig (optional, falls benötigt)
#char.create_random_set()

# Konvertiere die Statistiken in einen DataFrame
df = char_stats_to_dataframe(char)

# Streamlit-Anwendung
st.title("Charakterstatistiken: {}".format(selected_job))
st.write("Dies ist eine Tabelle mit den Statistiken des Charakters.")

# Zeige den DataFrame in Streamlit an
st.dataframe(df.set_index("Name"))

st.button("Roll Max")