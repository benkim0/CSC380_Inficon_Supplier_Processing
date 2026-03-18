import json
import pandas as pd
from fill_pdf_form import autofill_pdf_with_matches, extract_pdf_fields
from similarity_test import match_questions
from vector_embedding_model import load_embedding_model


def main():
    model = load_embedding_model()

    # Load your PDF and form/confluence data
    with open("form_data.json") as f:
        form_fields = json.load(f)
    with open("confluence_data.json") as f:
        confluence_data = json.load(f)

    form_df = pd.DataFrame(form_fields)
    conf_df = pd.DataFrame(confluence_data)

    # Run your embedding matcher
    match_results = match_questions(model, form_df, conf_df, threshold=0.8)

    # Open PDF and extract fields
    fields, pdf = extract_pdf_fields("toy_pdf.pdf")

    # Fill the PDF using matches
    filled_pdf = autofill_pdf_with_matches(pdf, fields, match_results, key="question_text")

    # Save the final PDF
    filled_pdf.save("output_pdf.pdf")
    print("PDF saved as output_pdf.pdf")


if __name__ == "__main__":
    main()