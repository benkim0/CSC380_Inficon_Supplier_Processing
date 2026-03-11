import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from transformers import pipeline

#FOR PDF??

PDF_PATH = "toy_pdf.pdf"
LLM_MODEL = "mpt-7b-instruct"
MAX_LINES = 500

def ocr_pdf(filepath):
    pages = convert_from_path(filepath)
    ocr_lines = []

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        lines = text.split("\n")
        ocr_lines.extend([line.strip() for line in lines if line.strip()])
    return ocr_lines

def extract_labels_with_llm(ocr_lines):
    llm = pipeline("text-generation", model=LLM_MODEL)

    chunks = [ocr_lines[i:i+MAX_LINES] for i in range(0, len(ocr_lines), MAX_LINES)]
    all_labels = []

    for chunk in chunks:
        text_chunk = "\n".join(chunk)
        prompt = f"""
You are extracting form field labels from a document. 
Ignore legal text, instructions, examples, or any explanatory text. 
Return ONLY the form field labels, one per line.

{text_chunk}
"""
        output = llm(prompt, max_new_tokens=500)[0]['generated_text']
        labels = [line.strip() for line in output.split("\n") if line.strip()]
        all_labels.extend(labels)

    return all_labels

