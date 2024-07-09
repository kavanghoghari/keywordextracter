# OCR and Keyword Extraction

This project processes images and PDF files to extract text, translate it, and generate keywords. The keywords are extracted from the translated text and associated with the respective file names.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

1. **Clone the repository** (if applicable) or create a project directory:
    ```bash
    mkdir keyword_extraction
    cd keyword_extraction
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv ocr_env
    source ocr_env/bin/activate
    ```

3. **Install required packages**:
    ```bash
    pip install pytesseract Pillow pdf2image googletrans==4.0.0-rc1 rake_nltk
    ```

4. **Download Tesseract language data**:
    ```bash
    mkdir -p ~/tessdata
    wget https://github.com/tesseract-ocr/tessdata/raw/master/hin.traineddata -P ~/tessdata/
    wget https://github.com/tesseract-ocr/tessdata/raw/master/guj.traineddata -P ~/tessdata/
    ```

5. **Install NLTK data**:
    ```bash
    python -m nltk.downloader stopwords
    python -m nltk.downloader punkt
    ```

## Directory Structure

Ensure your directory structure looks like this:
keyword_extraction/
├── images/
│ ├── image1.jpeg
│ ├── image2.png
│ ├── sample_pdf.pdf
├── keywords.py
├── ocr_env/
└── output_keywords.txt

