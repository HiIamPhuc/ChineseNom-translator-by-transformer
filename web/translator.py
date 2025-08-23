import streamlit as st
from utils.translate import generate_translation_batch
import os
from dotenv import load_dotenv

# Set the model directory
load_dotenv()
MODEL_DIR = os.getenv("MODEL_DIR", "../models/translation/mt5-nom-translator")

# Streamlit UI
st.title("ChineseNom Translator")

# Input area for Chinese-Nom text
input_text = st.text_area("Enter Chinese-Nom text:", height=200)

# Translate button
if st.button("Translate"):
    if input_text.strip():
        input = input_text.strip().split()
        print(input)

        # Perform translation
        translated_text = generate_translation_batch(input, MODEL_DIR, batch_size=16)
        print(translated_text)
        # Display the translated text
        st.text_area("Translated Text:", '\n'.join(translated_text), height=200, disabled=True)
    else:
        st.warning("Please enter some text to translate.")