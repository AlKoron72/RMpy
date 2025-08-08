import streamlit as st
import pandas as pd
import os
#from Char import Char
from SHORTS import SHORTS
from Rolls import Rolls

roller = Rolls(100)

if "show_info" not in st.session_state:
    st.session_state["show_info"] = False
if "info_time" not in st.session_state:
    st.session_state["info_time"] = 0

# Funktion, um die Statistiken eines Char-Objekts in einen DataFrame zu konvertieren
def char_stats_to_dataframe(char_obj) -> pd.DataFrame:
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

def get_max_value_for(short_str: str) -> int:
    searched_for = 0
    for stat in dude.Stats:
        if stat == short_str:
            searched_for = stat.max_value
    return searched_for

@st.dialog("Do your farty things")
def do_dialog(long_str:str, short_str:str):
    st.write(f"{long_str} ({short_str})")
    st.write(f"rolled a {roller.roll()}")
    if st.button("got it!"):
        st.rerun()

# Prüfe, ob Bob übergeben wurde
if "bob" in st.session_state:
    dude = st.session_state["bob"]
    #print(bob.get)
    st.write(f"{dude.name} wurde übergeben:")
    
    with st.expander("Mehr Infos anzeigen"):
        st.text(f"Hier stehen zusätzliche Details.\nAlter:    {dude.age}\nVolk:     {dude.race}")
        st.text(f"Name:{dude.name:>23}")
        st.text(f"Alter:{dude.age:>25}")
        st.text(f"Beruf:{dude.job.name:>31}")
        st.text(f"{dude.Stats[-1].name}:{dude.Stats[-1].max_value:>31}")
        st.text(f"Stats of {dude.name}: {dude}")

    #st.write(str(bob))

    # Konvertiere die Statistiken in einen DataFrame
    df = char_stats_to_dataframe(dude)

    # Streamlit-Anwendung
    st.title("Charakterstatistiken:")
    st.write("Dies ist eine Tabelle mit den Statistiken des Charakters.")

    # Zeige den DataFrame in Streamlit an
    st.dataframe(df.set_index("Name"))

    if st.button("Roll Max for all 10"):
        #st.write(bob.Stats[0])
        for stat in dude.Stats:
            stat.set_max_value(0)
#            stat.max_value = stat.set_max_value(stat.value)
            st.write(f"{stat.name}: {stat.value} / {stat.max_value}")

    button_names = list(SHORTS)
    pill_names = list()
    for pn in SHORTS:
        if dude.get_value_for_stat(pn, True) == 0:
            pill_names.append(pn.name)
    pill_selection = st.pills("Höchstwert Würfeln für", pill_names, selection_mode="multi")
    st.markdown(f"Your selected options: {pill_selection}.")
    
    if st.button("Roll for your choice"):
        if len(pill_selection) == 0:
            st.markdown("nichts ausgewählt")
        else:
            for ps in pill_selection:
                huh = get_max_value_for(ps)
                st.markdown(f"{ps}: {huh} max")


    cols = st.columns(len(button_names))
    for i, (col, short) in enumerate(zip(cols, button_names)):
        if get_max_value_for(str(short.name)) != 0:
            st.write(f"value for {short.name} is {dude.Stats.get_max_value_for(short.name)}")
        if col.button(short.name):
            st.write(f"Button für {short.value} ({short.name}) geklickt!")
            do_dialog(short.value, short.name)


else:
    st.write("Kein Charakter übergeben.")