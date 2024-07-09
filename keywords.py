import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from googletrans import Translator
from rake_nltk import Rake
import os

# Set TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = os.path.expanduser('~/tessdata/')

# Initialize the Translator
translator = Translator()

def ocr_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang='hin+guj')
    return text

def ocr_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ''
    for page in pages:
        text += pytesseract.image_to_string(page, lang='hin+guj')
    return text

def translate_text(text, dest_language='en'):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = list(set(rake.get_ranked_phrases()))  # Remove duplicates
    return keywords

def process_text_from_image(image_path):
    text = ocr_from_image(image_path)
    translated_text = translate_text(text)
    keywords = extract_keywords(translated_text)
    return keywords

def process_text_from_pdf(pdf_path):
    text = ocr_from_pdf(pdf_path)
    translated_text = translate_text(text)
    keywords = extract_keywords(translated_text)
    return keywords

def process_files_in_directory(directory):
    results = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            keywords = process_text_from_image(file_path)
        elif filename.endswith('.pdf'):
            keywords = process_text_from_pdf(file_path)
        else:
            continue
        results[filename] = keywords
    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as f:
        for filename, keywords in results.items():
            f.write(f"Keywords from {filename}:\n")
            f.write(", ".join(keywords) + "\n\n")

# Directory containing images and PDFs
directory = 'images'

# Process the files and save the results
results = process_files_in_directory(directory)
save_results_to_file(results, 'output_keywords.txt')
