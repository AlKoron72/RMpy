import streamlit as st

def show_tab1_content(create_button_clicked):
    """
    Zeigt den Inhalt für "Tab 1: Eingabe".

    Args:
        create_button_clicked (bool): Gibt an, ob der 'Create'-Button geklickt wurde.
    """
    st.write("Dies ist der Inhalt für Tab 1. Hier könnten Eingabefelder sein.")
    st.text_input("Geben Sie etwas ein", key="input_tab1")

    # Zeige diesen Inhalt nur an, wenn der Create-Button geklickt wurde
    if create_button_clicked:
        st.markdown("---")
        st.subheader("Neuer Inhalt nach dem Klick auf 'Create'")
        st.write("Sie haben den 'Create'-Button geklickt. Hier ist weiterer Inhalt für die Eingabe.")
        st.text_area("Hier können Sie Notizen hinzufügen", key="notes_tab1")
        st.button("Speichern Sie Notizen", key="save_notes") # Beispiel für einen weiteren Button
