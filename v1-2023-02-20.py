import streamlit as st
import openai

st.write("**✨ AI GENERATED IMAGES FROM PROMPT ✨**")

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Define the prompt for the model 
prompt = st.text_input("prompt: ")

# Generate text using the DALL-E model
response = openai.Image.create(
    prompt=prompt,
    n = 1,
    size="512x512",
)

# Get the URL of the generated image
image_url = response['data'][0]['url']

# Display the generated image
st.image(image_url, width=512)

# End of the app
st.write("**THE END ✨**")
st.write("**Developed by Aster Volta & Ana Cristina Olvera.**")
