import streamlit as st
import openai

# Initialize OpenAI API key (make sure to set your key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate a summary from the uploaded note
def generate_summary(note_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please summarize the following text:\n\n{note_text}",
        max_tokens=150,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary

# Function to generate Q&A based on the uploaded note
def generate_qa(note_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a question and answer set based on the following text:\n\n{note_text}",
        max_tokens=200,
        temperature=0.5,
    )
    q_and_a = response.choices[0].text.strip()
    return q_and_a

# Function to answer questions based on the uploaded note
def answer_question(note_text, question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Based on the following note, answer the question:\n\nNote: {note_text}\n\nQuestion: {question}",
        max_tokens=150,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

# Streamlit app interface
st.title("Note-Taking and Q&A App")

# Upload note section
uploaded_file = st.file_uploader("Upload your lecture note (Text file)", type=["txt"])
if uploaded_file is not None:
    note_text = uploaded_file.read().decode("utf-8")
    st.write("*Uploaded Note:*")
    st.text_area("Lecture Note", note_text, height=300)

    # Summary generation
    if st.button("Generate Summary"):
        summary = generate_summary(note_text)
        st.write("*Summary:*")
        st.write(summary)
    
    # Q&A generation
    if st.button("Generate Q&A"):
        q_and_a = generate_qa(note_text)
        st.write("*Q&A based on the Note:*")
        st.write(q_and_a)
    
    # Ask question about the note
    st.write("### Ask a Question about the Note")
    question = st.text_input("Enter your question here:")
    if st.button("Get Answer"):
        answer = answer_question(note_text, question)
        st.write("*Answer:*")
        st.write(answer)