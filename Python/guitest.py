import json
import pandas as pd
import sys

#from Python.fill_docx_form import autofill_docx
#from fill_docx_form import extract_docx_fields
from fill_pdf_form import autofill_pdf, extract_pdf_fields
from similarity_test import match_questions
from vector_embedding_model import load_embedding_model


def main():
    print("working")
    model = load_embedding_model()
    with open("C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\confluence_data.json") as f:
        confluence_data = json.load(f)

    conf_df = pd.DataFrame(confluence_data)
    input_path = sys.argv[1]
    pdf_fields, pdf = extract_pdf_fields(input_path)
    pdf_df = pd.DataFrame([
        {
            "question_text": f["field_name"].strip().lower(),
            "field_name": f["field_name"]
        }
        for f in pdf_fields
    ])
    pdf_match_results = match_questions(model, pdf_df, conf_df, threshold=0.8)
    a = sys.argv[1].split('\\')
    output_path = "output_" + (a[len(a) - 1])
    autofill_pdf(pdf, pdf_fields, pdf_match_results, output_path)

# doc_fields, doc = extract_docx_fields("toy_pdf.docx")
#docx_df = pd.DataFrame([
#    {
#        "question_text": f["field_name"].strip().lower(),
#       "field_name": f["field_name"]
#    }
#    for f in doc_fields
# ])
# doc_match_results = match_questions(model, docx_df, conf_df, threshold=0.8)
# autofill_docx("toy_pdf.docx", doc_fields, doc_match_results, "output_doc.docx")

if __name__ == "__main__":
    main()