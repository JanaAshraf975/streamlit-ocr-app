import cv2
import numpy as np
from PIL import Image
import streamlit as st
import pytesseract
import io  


try:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
except:
    st.warning("Tesseract path not set. Ensure Tesseract is installed and path is correct.")

st.title("Advanced Document Scanner Application")
st.write("Upload an image of a document to extract text using OCR with image preprocessing.")


upload = st.file_uploader("Please upload an image", type=["jpg", "png", "jpeg"], 
                          help="Supported formats: JPG, PNG, JPEG. Max size: 5MB")

def preprocess_image(img_array):

    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    return edged  

def extract_text(img_pil, lang='eng'):

    img_array = np.array(img_pil)
    processed_img = preprocess_image(img_array)
    processed_pil = Image.fromarray(processed_img)
    
    try:
        text = pytesseract.image_to_string(processed_pil, lang=lang)
        return text.strip()  
    except Exception as e:
        return f"Error in OCR: {str(e)}. Check image quality or language."

if upload is not None:
    
    if upload.size > 5 * 1024 * 1024:  # 5MB
        st.error("File too large! Please upload an image smaller than 5MB.")
    else:
        img = Image.open(upload)
        img_array = np.array(img)
        
        
        st.subheader("Original Image")
        st.image(img, caption="Uploaded Image" ,use_column_width=True)
        
        
        lang = st.text_input("Enter Language Code (e.g., 'eng' for English, 'ara' for Arabic)", 
                             value="eng", help="Common codes: eng, ara, fra, spa")
        
        if st.button("Extract Text") and lang.strip():  
            with st.spinner("Processing image and extracting text..."):
                text = extract_text(img, lang=lang)
                
                if text.startswith("Error"):
                    st.error(text)
                else:
                    st.subheader("Extracted Text")
                    st.text_area("Extracted Content:", text, height=300)
                    
                    
                    st.download_button(
                        label="Download Text as TXT",
                        data=text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
        
        
        if st.checkbox("Show Preprocessed Image"):
            processed_img = preprocess_image(img_array)
            st.subheader("Preprocessed Image (for OCR)")
            st.image(processed_img, caption="Enhanced for better accuracy", use_column_width=True)

else:
    st.info("Please upload an image to get started.")
