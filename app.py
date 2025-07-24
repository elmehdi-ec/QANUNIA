import streamlit as st
from qanunia_core.patient_manager import create_patient_record
from qanunia_core.ia_assistant import suggest_diagnosis
from ui.patient_form import patient_form

st.set_page_config(page_title="QANUNIA", layout="wide")
st.title("🩺 QANUNIA – Plateforme médicale pour cabinets")

patient_data = patient_form()

if patient_data:
    diagnosis = suggest_diagnosis(patient_data)
    st.subheader("🧠 Suggestion IA")
    st.info(diagnosis)

    if st.button("💾 Enregistrer le dossier patient"):
        create_patient_record(patient_data)
        st.success("✅ Dossier enregistré avec succès !")
