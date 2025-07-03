import streamlit as st
from transformers import pipeline

st.title("Simple AI Story Generator")

prompt = st.text_input("Enter a story prompt:")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        st.info("Generating story...")

        generator = pipeline("text-generation", model="gpt2")

        result = generator(prompt, max_length=100, num_return_sequences=1)
        story = result[0]['generated_text']

        st.subheader("Generated Story")
        st.write(story)
