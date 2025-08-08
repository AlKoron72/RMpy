import streamlit as st
import pandas as pd
from SHORTS import SHORTS

row_labels = []
columns = []
for s in SHORTS:
    row_labels.append(s.name)
    row_labels.append(s.name)

# Daten für die Tabelle
columns = ["Name"] + [col for col in columns]
data = {
    "Name": row_labels,
    **{col: [0] * len(row_labels) for col in columns[1:]},  # Dummy-Werte setzen
}

# DataFrame erstellen
df = pd.DataFrame(data)

# Mit st.data_editor anzeigen
edited_df = st.data_editor(df, key="stats_editor", num_rows="fixed")

# Aktionen nach Änderungen (z.B. Werte speichern und Berechnungen)
if st.button("Änderungen übernehmen"):
    st.write("Überarbeitete Tabelle:")
    st.write(edited_df)

    # Hier können weitere Aktionen auf Basis von edited_df durchgeführt werden.
