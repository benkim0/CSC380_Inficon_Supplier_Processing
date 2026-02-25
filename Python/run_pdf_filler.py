from database_handler import load_form_data, load_confluence_data
from extract import extract_pdf_fields
from similarity_test import match_questions
from autofill_engine import autofill_form
from fill_pdf_form import fill_pdf_form
from vector_embedding_model import load_embedding_model

def main():
    model = load_embedding_model()
    conf_df = load_confluence_data("confluence_data.json")
    form_df = load_form_data("form_data.json")

    form_fields = extract_pdf_fields("PF30.pdf")

    match_results = match_questions(model, form_df, conf_df)
    filled_fields = autofill_form(form_fields, match_results)

    for f in filled_fields:
        if f["field_type"] == "checkbox":
            if not f.get("options"):
                f["options"] = ["Yes", "No"]

            val = f.get("value")
            if val in [True, 1]:
                f["value"] = "Yes"
            elif val in [False, 0]:
                f["value"] = "No"
            elif val not in ["Yes", "No"]:
                f["value"] = None

    fill_pdf_form("PF30.pdf", "PF30_filled.pdf", filled_fields)

if __name__ == "__main__":
    main()