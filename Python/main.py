import json
import pandas as pd
from Python.fill_pdf_form import autofill_pdf_form
from similarity_test import match_questions
from vector_embedding_model import load_embedding_model


def main():
    model = load_embedding_model()
    with open("form_data.json") as f:
        form_fields = json.load(f)
    with open("confluence_data.json") as f:
        confluence_data = json.load(f)

    form_df = pd.DataFrame(form_fields)
    conf_df = pd.DataFrame(confluence_data)

    match_results = match_questions(model, form_df, conf_df, threshold=0.80)

    autofill_results = []
    for match in match_results:
        autofill_results.append({
            "form_question_id": match["form_question"],
            "answer": match["answer"],
            "decision": match["decision"],
            "field_type": match["field_type"]
        })

    autofill_pdf_form("toy_pdf.pdf", "output_pdf.pdf", form_fields, autofill_results, key="question_text")


if __name__ == "__main__":
    main()