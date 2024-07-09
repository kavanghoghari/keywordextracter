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


- **images/**: Directory containing the image and PDF files to be processed.
- **keywords.py**: The main script to run the OCR and keyword extraction process.
- **ocr_env/**: Virtual environment directory.
- **output_keywords.txt**: Output file where the keywords for each file will be saved.

## Script Explanation

### `keywords.py`

This script processes images and PDF files to extract text using OCR, translates the text to English, and extracts keywords using the RAKE algorithm.

#### Functions

- **ocr_from_image(image_path)**: Extracts text from an image file.
- **ocr_from_pdf(pdf_path)**: Extracts text from a PDF file.
- **translate_text(text, dest_language='en')**: Translates the extracted text to English.
- **extract_keywords(text)**: Extracts keywords from the translated text.
- **process_text_from_image(image_path)**: Processes an image file to extract and translate text, then extract keywords.
- **process_text_from_pdf(pdf_path)**: Processes a PDF file to extract and translate text, then extract keywords.
- **process_files_in_directory(directory)**: Processes all image and PDF files in the specified directory.
- **save_results_to_file(results, output_file)**: Saves the extracted keywords to a text file.

#### Usage

1. **Set TESSDATA_PREFIX environment variable**:
    ```python
    os.environ['TESSDATA_PREFIX'] = os.path.expanduser('~/tessdata/')
    ```

2. **Initialize the Translator**:
    ```python
    translator = Translator()
    ```

3. **Run the Script**:
    ```python
    python3 keywords.py
    ```

### Example Usage

The script will process all images and PDF files in the `images` directory and save the results to `output_keywords.txt`.

## Running the Script

1. **Activate the virtual environment**:
    ```bash
    source ocr_env/bin/activate
    ```

2. **Run the script**:
    ```bash
    python3 keywords.py
    ```

3. **Check the output**:
    The keywords for each file will be saved in `output_keywords.txt` in the following format:

    ```
    Keywords from image1.jpeg:
    keyword1, keyword2, keyword3, ...

    Keywords from sample_pdf.pdf:
    keyword1, keyword2, keyword3, ...
    ```

## Troubleshooting

- Ensure the Tesseract language data files are correctly downloaded and placed in the `~/tessdata/` directory.
- If any module is missing, install it using `pip install <module_name>`.
- Ensure that the image and PDF files are in the correct format and directory.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request
