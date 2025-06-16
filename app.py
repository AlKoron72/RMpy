import streamlit as st
from Char import Char
from content.tab1_content import show_tab1_content

def main():
    st.set_page_config(layout="wide") # Setzt das Seitenlayout auf "wide" für bessere Nutzung der Bildschirmfläche

    # Initialisiere den Session-State, wenn er noch nicht existiert
    if 'create_button_clicked' not in st.session_state:
        st.session_state.create_button_clicked = False

    # Erstelle zwei Spalten mit einer 30/70 Aufteilung
    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.header("Aktionen") # Überschrift für die linke Spalte
        if st.button("➕ Create"): # Hier wurde das Plus-Symbol hinzugefügt
            st.session_state.create_button_clicked = True # Setze den Zustand auf True, wenn der Button geklickt wird
            st.session_state.bob = Char("Bob", 15)
            st.success("Create-Button wurde geklickt!")
            # Hier kannst du die Logik für den 'Create'-Vorgang hinzufügen
            # Zum Beispiel: Datenbankeintrag erstellen, neues Formular anzeigen etc.

    with col2:
        st.header("Prozessschritte") # Überschrift für die rechte Spalte

        # Erstelle Tabs für die weiteren Prozessschritte
        tab1, tab2, tab3 = st.tabs(["Tab 1: Eingabe", "Tab 2: Analyse", "Tab 3: Ergebnis"])

        with tab1:
            show_tab1_content(st.session_state.create_button_clicked)
        with tab2:
            st.write("Dies ist der Inhalt für Tab 2. Hier könnten Analysedaten oder Diagramme angezeigt werden.")
            st.area_chart({"Daten A": [10, 20, 15, 30], "Daten B": [5, 15, 25, 20]})
            if st.session_state.create_button_clicked:
                st.write(f"Der Char ist {st.session_state.bob.name} und hat {st.session_state.bob.age} Jahre.")
                st.write(st.session_state.bob)
        with tab3:
            st.write("Dies ist der Inhalt für Tab 3. Hier könnten die finalen Ergebnisse oder Berichte präsentiert werden.")
            st.markdown("---") # Trennlinie
            st.write("**Zusammenfassung der Ergebnisse:**")
            st.write("Ihre Daten wurden erfolgreich verarbeitet und analysiert.")

            if st.session_state.create_button_clicked:
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                st.write(f"ddd{st.session_state.bob.Stats.pop(-1)}ddd")
                #st.write(f"Left-Over Stats:\n{st.session_state.bob}")

if __name__ == "__main__":
    main()
