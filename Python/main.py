import json

import pandas as pd
from pypdf import PdfReader
from database_handler import load_form_data, load_confluence_data
from similarity_test import match_questions
from autofill_engine import autofill_form
from fill_pdf_form import fill_pdf_form
from vector_embedding_model import load_embedding_model

def main():
    input_pdf = "toy_pdf.pdf"
    output_pdf = "completed_toy_pdf.pdf"

    with open("form_data.json", "r", encoding="utf-8") as f:
        form_fields = json.load(f)

    with open("confluence_data.json", "r", encoding="utf-8") as f:
        conf_data = json.load(f)

    conf_df = pd.DataFrame(conf_data)
    form_df = pd.DataFrame(form_fields)
    model = load_embedding_model()
    match_results = match_questions(model, form_df, conf_df)
    filled_fields = autofill_form(form_fields, match_results)

    reader = PdfReader(input_pdf)
    pdf_fields = reader.get_fields()

    field_map = {
        "F1": "Company Name",
        "F2": "A Subsidiary/Division of",
        "F3": "Street Address",
        "F4": "Country",
        "F5": "City",
        "F6": "State",
        "F7": "Zip",
        "F8": "County Name",
        "F9": "Contact Name",
        "F10": "Contact Phone",
        "F11": "Toll Free",
        "F12": "Fax",
        "F13": "Email Address",
        "F14": "Accepts Credit Card",
        "F15": "Web Site Address",
        "F16": "DUNS Number",
        "F17": "Federal Identification Number",
        "F18": "Incorporated",
        "F19": "Avg of Employees",
        "F20": "Annual Revenue",
        "F21": "SAM",
        "F22": "SAM Expiration Dt",
        "F23": "Global DUNS No",
        "F24": "Global Parent Name",
        "F25": "Service-Disabled Vet",
        "F26": "State / Local Govt",
        "F27": "Econ Disadv Woman-Owned",
        "F28": "Woman-Owned",
        "F29": "Foreign Owned",
        "F30": "Educational Institution",
        "F31": "Veteran Owned",
        "F32": "Non-Profit",
        "F33": "Fed Govt",
        "F34": "8A",
        "F35": "HubZone",
        "F36": "Black American",
        "F37": "Asian-Indian American",
        "F38": "Hispanic American",
        "F39": "Asian-Pacific American",
        "F40": "Native American",
        "F41": "None",
        "F42": "Alaskan-Native",
        "F43": "Native Hawaiian",
        "F44": "American Indian",
        "F45": "NAICS1",
        "F46": "NAICS2",
    }

    fill_pdf_form(input_pdf, output_pdf, filled_fields, field_map)

    print("PDF autofill complete!")

if __name__ == "__main__":
    main()