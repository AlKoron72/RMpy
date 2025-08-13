# collects files in folders and mmakes list of them
# for st.selectboxes to use as basis

 
import streamlit as st
import os

def get_job_classes(directory="jobs"):
    return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]

def get_races(directory="races"):
    return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]

def get_files_in_dir(directory:str ="jobs"):
    try:
        return [f[:-3] for f in os.listdir(directory) if f.endswith(".py") and not f.startswith("__")]
    except FileNotFoundError:
        st.error(f"{directory} not found")
        return []
    except Exception as e:
        st.warning(f"Fehler beim Lesen von {directory}: {e}")
        return []