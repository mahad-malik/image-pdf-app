import streamlit as st
from transformers import pipeline
from PIL import Image
from streamlit_pdf_viewer import pdf_viewer
from PyPDF2 import PdfReader 
# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_content(text):
     # Use GPT-Neo for text generation
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

    # Create a more directive and specific prompt for humor
    prompt = (
        "Here’s a snippet from a serious document:\n\n"
        f"\"{text[:300]}\"\n\n"  # Include only the first 300 characters to avoid overwhelming the model
        "Turn this into a question:"
    )
    
    # Generate humorous content
    result = generator(prompt, do_sample=True, max_new_tokens=50, num_return_sequences=1)
    
    # Print and return the generated text
    generated_text = result[0]['generated_text']
    print(generated_text)
    return generated_text

# Function to display PDF directly
def display_pdf(uploaded_file):
    if uploaded_file is not None:
        # Read the PDF file bytes
        pdf_bytes = uploaded_file.read()        
        # Display PDF using a third-party component
        pdf_viewer(pdf_bytes, width=800)  # Adjust width as needed

def pdf_reader_app():
    # st.set_page_config(page_title="PDF Extractor", page_icon="")
    st.title("Extract Content from PDF")   
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        # Display the PDF directly in the app
        st.write("Displaying PDF:")
        display_pdf(uploaded_file)
        
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(uploaded_file)

        # Generate  content
        if st.button('Generate Content'):
            with st.spinner('Generating content...'):
                simple_content = generate_content(text)
            st.subheader("Here's something from your PDF:")
            content= simple_content.split("Turn this into a question:")
            st.write(content[1])


# if __name__ == '__main__':
#     main()
