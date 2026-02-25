import os
from pypdf import PdfReader
from fill_pdf_form import fill_pdf_form

def process_file(filepath, match_results):
    file_type = detect_file_type(filepath)

    if file_type == "fillable_pdf":
        return fill_pdf_form(filepath, match_results)

    elif file_type == "docx":
        return fill_docx_form(filepath, match_results)

    elif file_type == "csv":
        return fill_csv_form(filepath, match_results)

    elif file_type == "non-fillable_pdf":
        return fill_over_pdf(filepath, match_results)

    else:
        raise ValueError("Unsupported File Type")

def detect_file_type(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        if is_fillable_pdf(filepath):
            return "fillable_pdf"
        else:
            return "non-fillable_pdf"

    elif ext == ".docx":
        return "docx"

    elif ext == ".csv":
        return "csv"

    else:
        return "unknown"

def is_fillable_pdf(filepath):
    reader = PdfReader(filepath)
    return "/AcroForm" in reader.trailer["/Root"]
