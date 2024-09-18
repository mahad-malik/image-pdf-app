# Image and PDF Processing App

This is a **Streamlit-based web application** with two main functionalities:
1. **Image-to-Text Story Generator**: Extracts text from an uploaded image and generates a story based on that text.
2. **PDF Content Extractor**: Extracts text from an uploaded PDF and generates transformed or humorous content from it.

## Features

- **Image-to-Text Story Generator**:
  - Upload an image in JPG, JPEG, or PNG format.
  - Extracts the image’s text using the `Salesforce/blip-image-captioning-base` model.
  - Generates a short story based on the extracted text using GPT-2.

- **PDF Content Extractor**:
  - Upload a PDF document.
  - Extracts the text from the PDF.
  - Generates humorous or transformed content from the extracted text using GPT-Neo.

## How to Run the Project

To run the app locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/image-pdf-app.git`
2. Install the necessary dependencies:
   ```bash
   pip install streamlit transformers Pillow
Run the Streamlit app:
streamlit run app.py

Requirements:
Streamlit
Transformers (Huggingface)
Pillow (for image processing)
