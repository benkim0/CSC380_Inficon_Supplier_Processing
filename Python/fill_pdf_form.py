from pypdf import PdfReader, PdfWriter
import fitz

def extract_pdf_fields(pdf_path):
    pdf = fitz.open(pdf_path)
    fields = []

    if hasattr(pdf, "widgets") and pdf.widgets():
        fields = pdf.widgets()
    else:
        for page in pdf:
            if hasattr(page, "widgets") and page.widgets():
                fields.extend(page.widgets())

    if not fields:
        print("No fields found in this pdf")
        return []

    field_list = []
    for f in fields:
        print(f"Field Name: {f.field_name}, Rect: {f.rect}")
        field_list.append({
            "field_name": f.field_name,
            "rect": f.rect,
            "field_type": f.field_type.name if hasattr(f.field_type, "name") else str(f.field_type)
        })
    return field_list, pdf


def autofill_pdf_with_matches(pdf, fields, match_results, key="form_question_id"):
    match_map = {m[key].lower(): m for m in match_results if key in m}

    for page in pdf:
        for widget in page.widgets():
            field_name = widget.field_name
            match = match_map.get(field_name.lower())
            if not match:
                continue

            answer = match.get("answer")
            if answer is None:
                continue

            if widget.field_type.name == "Text":
                widget.field_value = str(answer)
                widget.update()
            elif widget.field_type.name == "Button":
                value = True if str(answer).lower() in ("yes", "true", "1") else False
                widget.field_value = value
                widget.update()

    return pdf