# streamlit-ocr-app
A Streamlit-based OCR application that extracts text from uploaded images using Tesseract, with image preprocessing (grayscale, denoising, edge detection) and support for multiple languages. Users can preview processed images and download extracted text as TXT files.


# Document Scanner Application 📝🔍

A simple **Streamlit-based OCR (Optical Character Recognition)** application that extracts text from uploaded images using **Tesseract OCR**.  
The app supports multiple languages, basic image preprocessing, and allows users to download extracted text as a `.txt` file.

---

## ✨ Features
- 📤 Upload images (`.jpg`, `.jpeg`, `.png`)
- 🌐 Extract text in multiple languages with **Tesseract**
- 🎛️ Image preprocessing (grayscale, denoising, edge detection)
- ⏳ Real-time text extraction with progress spinner
- 📥 Download extracted text as a `.txt` file
- ⚙️ Configurable settings via **Streamlit sidebar**

---

## 📂 Project Structure

📁 document-scanner-app
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation



---

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/document-scanner-app.git
   cd document-scanner-app
   ```
2. Install dependencies:
   
 ```

pip install -r requirements.txt
```

3. Install Tesseract OCR
:

Windows: Download from Tesseract at UB Mannheim

Linux (Ubuntu/Debian):

sudo apt install tesseract-ocr

macOS:

brew install tesseract


Set the Tesseract path in app.py (for Windows users):

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe

🚀 Run the Application
```
streamlit run app.py
```

📊 Example Workflow

Upload an image of a document.

Select or enter the language of the text (e.g., eng, ara, spa).

Preview the image and extracted text.

Download the extracted text as .txt.

🛠️ Future Improvements

🔎 Automatic language detection with langdetect

📑 PDF support using PyMuPDF

🎨 Advanced preprocessing (threshold, contrast enhancement)

🌐 Deploy on Streamlit Cloud

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

📜 License

This project is licensed under the MIT License.


⚡ This README is professional and clear — looks good for a **GitHub portfolio project**.  

Do you want me to also generate the `requirements.txt` file so your repo will be 100% re
