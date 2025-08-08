import streamlit as st
import pandas as pd

# Beispiel-Daten für die Tabelle
columns = ["Name", "Value", "Max", "Bonus", "Bonus-Race", "Total Bonus"]
# Abkürzungen und zufällige Werte für die Zeilen
row_labels = ["ST", "QU", "PR", "IN", "EM", "SD", "RE", "ME", "CO", "AG"]

# Dummywerte für das Beispiel
data = {
    "Name": row_labels,
    "Value": [50, 65, 70, 40, 55, 60, 75, 80, 45, 50],
    "Max": [90, 95, 100, 85, 90, 95, 80, 75, 70, 60],
    "Bonus": [10, 15, 20, 5, 10, 5, 25, 10, 10, 5],
    "Bonus-Race": [5, 5, 10, 0, 5, 5, 0, 5, 5, 0],
    "Total Bonus": [15, 20, 30, 5, 15, 10, 25, 15, 15, 5],
}

df = pd.DataFrame(data)

# `st.data_editor` verwendet, um die Tabelle darzustellen und zu bearbeiten
edited_df = st.data_editor(df, key="stats_table", num_rows="fixed")

# Geänderte Tabelle anzeigen
if st.button("Tabelle speichern"):
    st.write("Die geänderten Werte sind:")
    st.write(edited_df)
