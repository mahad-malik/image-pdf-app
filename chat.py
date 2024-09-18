from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import os
import streamlit as st
from PIL import Image

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]['generated_text']
    print(text)
    return text

# Define LLM for generating a story
def generate_story(scenario):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(scenario, max_length=50, truncation=True)
    return result[0]['generated_text']

def chat_app():
    # st.set_page_config(page_title='img 2 text story', page_icon="")
    st.header("Turn img into text story")
    uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)  
        st.image(image, caption='Uploaded Image.', use_column_width=True)


        with st.spinner('Extracting text from image...'):
            scenario = img2text(image)
        
        st.write(scenario)
        if st.button('Generate Content'):    
            with st.spinner('Generating story...'):
                story = generate_story(scenario)
            

            with st.expander("Story"):
                st.write(story)

# if __name__ == '__main__':
#     chat_app()
