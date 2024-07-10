import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from googletrans import Translator
from rake_nltk import Rake
import os
import re

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
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases()
    return keywords

def filter_keywords(keywords):
    meaningful_keywords = []
    for keyword in keywords:
        if re.search('[a-zA-Z]', keyword) and len(keyword) > 2:
            meaningful_keywords.append(keyword)
    return list(set(meaningful_keywords))  # Remove duplicates

def process_text_from_image(image_path):
    text = ocr_from_image(image_path)
    translated_text = translate_text(text)
    keywords = extract_keywords(translated_text)
    return filter_keywords(keywords)

def process_text_from_pdf(pdf_path):
    text = ocr_from_pdf(pdf_path)
    translated_text = translate_text(text)
    keywords = extract_keywords(translated_text)
    return filter_keywords(keywords)

def process_files_in_directory(directory):
    results = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            keywords = process_text_from_image(file_path)
            results[filename] = keywords
        elif filename.lower().endswith('.pdf'):
            keywords = process_text_from_pdf(file_path)
            results[filename] = keywords
    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as f:
        for filename, keywords in results.items():
            f.write(f"Keywords from {filename}:\n")
            f.write(", ".join(keywords) + "\n\n")

# Main execution
if __name__ == "__main__":
    directory = 'images'  # Directory containing images and PDFs
    output_file = 'output_keywords.txt'  # Output file to save keywords

    results = process_files_in_directory(directory)
    save_results_to_file(results, output_file)

    print(f"Keywords have been extracted and saved to {output_file}")
