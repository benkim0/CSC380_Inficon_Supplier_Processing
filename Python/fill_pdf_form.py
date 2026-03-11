from pypdf import PdfReader, PdfWriter

def autofill_pdf_form(input_path, output_path, form_fields, match_results, key="form_question_id"):
    match_map = {m[key]: m for m in match_results if key in m}
    reader = PdfReader(input_path)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    pdf_field_map = reader.get_fields() or {}

    for field_name, pdf_field in pdf_field_map.items():
        match = match_map.get(field_name)
        if not match:
            continue

        decision = match.get("decision")
        answer = match.get("answer")
        field_type = pdf_field.get("/FT")

        if decision == "autofill":
            if field_type == "/Tx":
                writer.update_page_form_field_values(reader.pages[0], {field_name: str(answer)})
            elif field_type == "/Btn":
                value = "/Yes" if answer else "/Off"
                writer.update_page_form_field_values(reader.pages[0], {field_name: value})

        elif decision == "review suggested":
            value = str(answer) if field_type == "/Tx" else ("/Yes" if answer else "/Off")
            writer.update_page_form_field_values(reader.pages[0], {field_name: value})

    with open(output_path, "wb") as f:
        writer.write(f)