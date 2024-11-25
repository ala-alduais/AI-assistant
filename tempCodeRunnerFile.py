import streamlit as st
import openai
import os
from openai import OpenAI
import google.generativeai as genai
from google.colab import userdata
from PIL import Image

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

st.title("AI Note-Taking and Image Generation Assistant")

# Sidebar for Navigation
st.sidebar.title("Features")
note_section = st.sidebar.checkbox("Notes with Images")
qna_section = st.sidebar.checkbox("Q&A")
image_gen_section = st.sidebar.checkbox("Image Generation")

# Note-Taking Section
if note_section:
    st.header("AI-Powered Note-Taking")
    note_input = st.text_area("Enter your notes here:", height=150)

    if st.button("Summarize Notes"):
        # Summarize the notes using OpenAI/Gemini
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"Summarize the following notes briefly:\n{note_input}",
            max_tokens=100
        )
        summary = response['choices'][0]['text'].strip()
        st.write("Summary:", summary)

        # Generate an image based on the summary
        if st.button("Generate Image for Notes"):
            image_prompt = f"Create an image illustrating the following notes: {summary}"
            image_response = openai.Image.create(
                prompt=image_prompt,
                n=1,
                size="1024x1024"
            )
            image_url = image_response['data'][0]['url']
            st.image(image_url, caption="Generated Image for Notes")

            # Q&A Section
if qna_section:
    st.header("Q&A Section")
    question = st.text_input("Ask a question based on your notes:")

    if st.button("Get Answer"):
        # Use OpenAI/Gemini API to answer questions based on notes
        qna_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Answer the following question based on these notes: {note_input}\nQuestion: {question}",
            max_tokens=150
        )
        answer = qna_response['choices'][0]['text'].strip()
        st.write("Answer:", answer)

        # Image Generation Section
if image_gen_section:
    st.header("Image Generation")
    image_prompt = st.text_input("Describe the image you want to generate:")

    if st.button("Generate Image"):
        # Generate image based on prompt using OpenAI API
        image_response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )
        image_url = image_response['data'][0]['url']
        st.image(image_url, caption="Generated Image")