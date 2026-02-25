from pypdf import PdfReader

def extract_pdf_fields(pdf_path):
    reader = PdfReader(pdf_path)

    if "/AcroForm" not in reader.trailer["/Root"]:
        print("PDF is not fillable")
        return []

    fields = reader.get_fields()
    form_fields = []

    for field_name, field_info in fields.items():
        field_type = field_info.get("/FT")
        options = field_info.get("/Opt")

        if field_type == "/Btn":
            simplified_type = "checkbox"
        elif field_type == "/Tx":
            simplified_type = "text"
        elif field_type == "/Ch":
            simplified_type = "dropdown"
        else:
            simplified_type = "text"

        if options:
            options = [str(opt) for opt in options]
        else:
            options = []

        form_fields.append({
            "form_question_id": field_name,
            "field_type": simplified_type,
            "options": options
        })

    return form_fields

if __name__ == "__main__":
    pdf_path = "PF30.pdf"
    fields = extract_pdf_fields(pdf_path)
    print("Extracted Fields:")
    for f in fields:
        print(f)