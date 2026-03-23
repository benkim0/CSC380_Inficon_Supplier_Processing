import json
import pandas as pd
from fill_pdf_form import autofill_pdf, extract_pdf_fields
from similarity_test import match_questions
from vector_embedding_model import load_embedding_model


def main():
    model = load_embedding_model()

    with open("confluence_data.json") as f:
        confluence_data = json.load(f)

    conf_df = pd.DataFrame(confluence_data)

    fields, pdf = extract_pdf_fields("toy_pdf.pdf")
    print("Fields found:", len(fields))
    for f in fields:
        print(f)

    pdf_df = pd.DataFrame([
        {
            "question_text": f["field_name"].strip().lower(),
            "field_name": f["field_name"]
        }
        for f in fields
    ])

    match_results = match_questions(model, pdf_df, conf_df, threshold=0.8)

    autofill_pdf("toy_pdf.pdf", "output_pdf.pdf", match_results)

if __name__ == "__main__":
    main()