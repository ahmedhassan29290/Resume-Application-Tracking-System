import streamlit as st
from pdf_utils import PDFUtils
from gemini_client import GeminiClient
from prompts import  get_interview_question,get_detailed_prompt

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("Resume ATS Tracking System")

# Instantiate GeminiClient
gemini_client = GeminiClient()

# Inputs from the user
title = st.text_input("Job Title:", key="title")
description = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# Buttons for user actions
submit3 = st.button("Evaluate Resume")
submit1 = st.button("Interview Questions")

# Get prompts
input_prompt = get_interview_question(title, description)
detailed_prompt = get_detailed_prompt(title, description)

# Process user input
if submit1:
    if uploaded_file is not None:
        pdf_content = PDFUtils.convert_pdf_to_image(uploaded_file)
        response = gemini_client.get_response(input_prompt, pdf_content, description)
        st.write(response)
    else:
        st.write("Please upload the resume")
    pass

elif submit3:
    if uploaded_file is not None:
        pdf_content = PDFUtils.convert_pdf_to_image(uploaded_file)
        response = gemini_client.get_response(detailed_prompt, pdf_content, description)
        st.write(response)
    else:
        st.write("Please upload the resume")
