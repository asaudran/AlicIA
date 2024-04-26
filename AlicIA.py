#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Configuration de la page
st.set_page_config(page_title="AlicIA", layout="wide")

def main():
    st.sidebar.title("AlicIA")
    st.sidebar.markdown("## Explorez nos services")

    # Tabs for different services
    tab1, tab2 = st.tabs(["Formulaire Étudiant", "Modèle de Coaching"])

    # Tab 1: Formulaire pour les élèves
    with tab1:
        st.header("Formulaire d'orientation pour les étudiants")
        st.markdown("### Veuillez renseigner vos informations")
        
        with st.form("student_form"):
            name = st.text_input("Nom")
            age = st.number_input("Âge", min_value=18, max_value=30)
            email = st.text_input("Email")
            school = st.text_input("École de commerce")
            how_found_us = st.selectbox("Comment avez-vous connu AlicIA ?", ["Réseaux sociaux", "Recommandation", "Événements", "Autre"])
            interested = st.radio("Êtes-vous intéressé par un coaching d'orientation professionnelle ?", ["Oui", "Non"])
            needs = st.text_area("Qu'attendez-vous d'un coaching ?")

            submitted = st.form_submit_button("Envoyer les données")
            if submitted:
                st.success("Merci, vos données ont été envoyées !")

    # Tab 2: Modèle de Coaching
    with tab2:
        st.header("Découvrez votre secteur idéal")
        st.markdown("### Complétez les informations suivantes pour une recommandation personnalisée")
        
        with st.form("coaching_model"):
            st.file_uploader("Importer vos bulletins")
            skills = st.text_area("Décrivez vos compétences principales")
            soft_skills = st.text_area("Listez vos soft skills")
            mad_skills = st.text_area("Avez-vous des MadSkills? Si oui, lesquelles?")
            activities = st.text_area("Activités extra-scolaires (par ex. clubs, sports, musique)")
            submit = st.form_submit_button("Analyser")
            
            if submit:
                # Simplified model decision logic
                sector, advice = recommend_sector(skills)
                st.success(f"Selon vos compétences, le secteur recommandé est : {sector}")
                st.markdown("### Conseils pour réussir dans ce secteur")
                st.markdown(advice)

def recommend_sector(skills):
    # Simple logic based on keywords for demonstration
    if "gestion" in skills.lower() or "finance" in skills.lower():
        sector = "Finance"
        advice = """- Rejoignez des stages en banque ou en gestion d'actifs.
                    - Participez à des séminaires sur les tendances financières.
                    - Développez une attitude professionnelle rigoureuse."""
    elif "communication" in skills.lower() or "marketing" in skills.lower():
        sector = "Marketing"
        advice = """- Engagez-vous dans des clubs de marketing de votre école.
                    - Suivez des cours en ligne sur le marketing numérique.
                    - Valorisez vos soft skills comme la créativité et la persuasion dans votre CV."""
    else:
        sector = "Informatique"
        advice = """- Participez à des hackathons et des projets de groupe.
                    - Apprenez des langages de programmation populaires via des cours certifiés.
                    - Montrez vos soft skills comme la résolution de problèmes et la gestion de projet."""
    
    return sector, advice

if __name__ == "__main__":
    main()

