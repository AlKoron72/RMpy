import streamlit as st

def show_character_inputs(job_classes, races, age_range):
    col1, col2, col3 = st.columns(3)
    selected_name = col1.text_input("Gib einen Namen ein", help="the name please")
    selected_more_name = col2.text_input("Gib einen Namenszusatz ein")
    col1, col2, col3 = st.columns(3)
    selected_job = col1.selectbox("Wähle Deine Klasse", job_classes, index=3)
    selected_race = col2.selectbox("Wähle Dein Volk", races, index=1, help="Hilfe zu den einzelnen Völkern gibt es nur für das jeweils ausgewählte.")
    age_help = "Alter eingeben oder auswählen.\nWenn größer 999, dann kann man die Option 'andere...' wählen."
    selected_age = col3.selectbox("Wähle Deine Alter", age_range, index=2, help=age_help)
    return selected_name, selected_more_name, selected_job, selected_race, selected_age

def show_assignment_explanation():
    st.subheader("Zuweisung der Werte zu Eigenschaften", divider="red")
    with st.expander("wenn eine Erklärung gebraucht wird:"):
        st.write("Für Deinen Charakter wurde bereits 10x gewürfelt.")
        st.write("Die Ergebnisse befinden sich in der linken Spalte (unter **Würfe**).")
        st.write("Du kannst diese Werte den Eigenschaften zuweisen, indem Du die Kreuzchen setzt.")
        st.write("-- Jeder nur ein Kreuz! -- dafür sorgt das Programm selbst --")
        st.text("Sobald Du einen Wert ausgewählt hast, werden die Auswirkungen Deiner Auswahl unten kommentiert.")
        st.write("- Werte mit einem Sternchen (&#9734;) sind für die Berechnung der Entwicklungspunkte verantwortlich, **für alle Klassen gleichermaßen.**")
        st.write("- Werte mit einem Pfeil nach oben (&#x2B06;) werden auf 90 angehoben, weil sie die Haupteigenschaften Deines Charakters und der gewählten Charakterklasse sind. Je nach Auswahl der Charakterklasse ändern sich auch die Haupteigenschaften.")
        st.warning("Erst wenn **alle 10 Werte** verteilt wurden, kannst Du die Verteilung speichern und für den Charakter übernehmen.") 
        st.write("- Welcher Wert noch fehlt, sieht man leicht in der Auswahlbeschreibung unter dem Feld.")
        st.error("Beachte, sind die Anfangswerte Deines Charakters. In einem nächsten Schritt wird für jeden Wert erneut gewürfelt, um den potentiellen Maximalwert zu ermitteln, den Dein Charakter im Laufe seiner Karriere erreichen kann, wenn er lang genug überlebt.")