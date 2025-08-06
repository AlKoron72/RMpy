import streamlit as st
import pandas as pd
import random

# Dummy-Daten: Ersetze dies durch char_stats_to_dataframe(bob)
# df = char_stats_to_dataframe(bob)
df = pd.DataFrame({
    "Name": ["STR", "DEX", "CON"],
    "Value": [12, 14, 11],
    "MAX": [15, 16, 13],
    "Bonus": [1, 2, 0],
    "Bonus-Race": [0, 1, 0],
    "Total Bonus": [1, 3, 0],
})

st.title("Charakterstatistiken mit Roll-Buttons")

# Stelle sicher, dass der Zustand für jeden Roll gespeichert wird
if "max_rolls" not in st.session_state:
    st.session_state["max_rolls"] = {}

# Tabelle "händisch" rendern, sodass jede Zeile einen Button enthält
for idx, row in df.iterrows():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([2,1,2,2,2,2,2])
    col1.write(row["Name"])
    col2.write(row["Value"])

    # Eindeutiger Key für jeden Button
    key = f"roll_{idx}"

    # Wenn schon gerollt wurde, zeige den Wert an, sonst Button
    if key in st.session_state["max_rolls"]:
        col3.write(st.session_state["max_rolls"][key])
    else:
        if col3.button("Roll", key=key):
            rolled = random.randint(1, 20)  # Beispiel: W20, passe ggf. an
            st.session_state["max_rolls"][key] = rolled
            st.experimental_rerun()  # Seite neu laden, damit Wert angezeigt wird

    col4.write(row["Bonus"])
    col5.write(row["Bonus-Race"])
    col6.write(row["Total Bonus"])