import json

from ai_testing import ocr_pdf, extract_labels_with_llm, PDF_PATH
import pandas as pd
from pypdf import PdfReader
from database_handler import load_form_data, load_confluence_data
from similarity_test import match_questions
from autofill_engine import autofill_form
from fill_pdf_form import fill_pdf_form
from vector_embedding_model import load_embedding_model
from extract_docx import extract_docx_questions, clean_lines

def main():
    filepath = "toy_pdf.docx"
    lines = extract_docx_questions(filepath)
    lines = clean_lines(lines)
    for line in lines:
        print(lines)
if __name__ == "__main__":
    main()