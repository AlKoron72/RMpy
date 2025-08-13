import json
import os
import streamlit as st

def save_char_to_file(bob, filename="char.json"):
    """
    Speichert das Char-Objekt als JSON-Datei.
    """
    try:
        # Annahme: bob hat die Attribute name, age, race, more_name und eine Stats-Liste mit name/value
        char_dict = {
            "name": bob.name,
            "age": bob.age,
            "race": bob.race,
            "more_name": getattr(bob, "more_name", ""),
            "stats": [
                {
                    "name": stat.name,
                    "value": stat.value,
                    "max_value": getattr(stat, "max_value", None)
                }
                for stat in bob.Stats
            ]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(char_dict, f, ensure_ascii=False, indent=2)
        st.success(f"Charakter wurde gespeichert: {filename}")
    except Exception as e:
        st.error(f"Fehler beim Speichern: {e}")

def load_char_from_file(filename="char.json", CharClass=None, StatClass=None):
    """
    Lädt einen Char-Charakter aus einer JSON-Datei.
    CharClass und StatClass sollten Konstruktoren/Fabriken für die jeweiligen Objekte sein.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            char_dict = json.load(f)
        # Erzeuge das Char-Objekt (optional: CharClass angeben)
        char_obj = CharClass(
            char_dict["name"],
            char_dict["age"],
            job=char_dict.get("job", "Unbekannt"),
            race=char_dict.get("race", "Unbekannt")
        )
        char_obj.more_name = char_dict.get("more_name", "")
        # Stats rekonstruieren
        char_obj.Stats = []
        for stat in char_dict["stats"]:
            stat_obj = StatClass(stat["name"], stat["value"])
            if "max_value" in stat:  # Optional
                stat_obj.max_value = stat["max_value"]
            char_obj.Stats.append(stat_obj)
        st.success(f"Charakter wurde geladen: {filename}")
        return char_obj
    except Exception as e:
        st.error(f"Fehler beim Laden: {e}")
        return None

# Beispiel für Update (hier: nur Name ändern, kann erweitert werden)
def update_char_name(bob, new_name):
    bob.name = new_name
    st.info(f"Name aktualisiert auf {new_name}")

# Beispiel für Delete
def delete_char_file(filename="char.json"):
    try:
        os.remove(filename)
        st.success(f"{filename} wurde gelöscht.")
    except Exception as e:
        st.error(f"{filename} konnte nicht gelöscht werden: {e}")