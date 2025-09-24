
import bootstrap

# 👇 Now safe to import other modules
import streamlit as st
from crewai.rag.config.types import RagConfigType

from run import run_bot
import os


# Call the function to load your custom CSS


st.title('Cipher Research Assistant 🧠✨')


with st.sidebar:
    st.header('Enter Research Details 📝')
    topic = st.text_input("Main topic of your research:")
    detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")

if st.button('Start Research 🚀'):
    if not topic or not detailed_questions:
        st.error("Please fill all the fields. 😥")
    else:
        user_input = f"Research Topic: {topic}\nDetailed Questions: {detailed_questions}"
        
        research_crew = run_bot(user_input)
        result = research_crew
        st.subheader("Results of your research project: 📜")
        st.markdown(result)
