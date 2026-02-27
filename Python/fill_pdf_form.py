from pypdf import PdfReader, PdfWriter

def fill_pdf_form(input_path, output_path, filled_fields, field_map):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    # Ensure proper AcroForm object
    if "/AcroForm" in reader.trailer["/Root"]:
        acro_form = reader.trailer["/Root"]["/AcroForm"].get_object()
        writer._root_object.update({"/AcroForm": acro_form})

    field_updates = {}
    for f in filled_fields:
        pdf_field_name = field_map.get(f["form_question_id"])
        value = f.get("value")
        if pdf_field_name and value is not None:
            if f.get("field_type") == "checkbox":
                field_updates[pdf_field_name] = "/Yes" if str(value).lower() in ["yes", "true", "1"] else "/Off"
            else:
                field_updates[pdf_field_name] = str(value)

    if not field_updates:
        print("No fields to update. Check your field_map and filled_fields.")
        return

    writer.update_page_form_field_values(writer.pages, field_updates)

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Filled PDF saved to {output_path}")