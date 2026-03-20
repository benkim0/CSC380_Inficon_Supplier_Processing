import json
import pandas as pd
from fill_pdf_form import autofill_pdf_with_matches, extract_pdf_fields
from similarity_test import match_questions
from vector_embedding_model import load_embedding_model


def main():
    model = load_embedding_model()

    with open("confluence_data.json") as f:
        confluence_data = json.load(f)

    conf_df = pd.DataFrame(confluence_data)

    fields, pdf = extract_pdf_fields("toy_pdf.pdf")

    pdf_df = pd.DataFrame([
        {
            "question_text": f["field_name"].strip().lower(),
            "field_name": f["field_name"]
        }
        for f in fields
    ])

    match_results = match_questions(model, pdf_df, conf_df, threshold=0.8)

    # filled_pdf = autofill_pdf_with_matches(pdf, fields, match_results, key="question_text")
    #
    # filled_pdf.save("output_pdf.pdf")
    # print("PDF saved as output_pdf.pdf")

    for m in match_results:
        print("PDF Field:", m.get("form_question"))
        print("Matched To:", m.get("confluence_question"))
        print("Answer:", m.get("answer"))
        print("Score:", m.get("similarity_score"))
        print("Decision:", m.get("decision"))
        print("\n")


if __name__ == "__main__":
    main()