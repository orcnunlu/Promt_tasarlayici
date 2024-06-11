import google.generativeai as genai
import streamlit as st

# Google Generative AI API anahtarınızı yapılandırın
API_KEY = "Kendi APİ KEY inizi girin"
genai.configure(api_key=API_KEY)

# Modeli başlatın
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

st.title("GPT Prompt Generator")

instruction = """
I want you to act as a GPT prompt generator,
I will send a topic, you have to generate a GPT prompt based
on the content of the topic, the prompt should start with
"I want you to act as ", and guess what I might do, and expand the prompt accordingly
Describe the content to make it useful.
"""

# Kullanıcıdan giriş al
question = st.text_input("Enter a topic:")

if st.button("Generate Prompt"):
    if question.strip():
        response = chat.send_message(instruction + question)
        st.write(f"Generated Prompt: {response.text}")
    else:
        st.write("Please enter a topic.")

# Uygulamayı çalıştırmak için aşağıdaki komutu terminalde kullanın:
# streamlit run app.py
