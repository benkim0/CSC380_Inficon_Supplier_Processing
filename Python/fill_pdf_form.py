from pypdf import PdfReader, PdfWriter

def fill_pdf_form(input_path, output_path, filled_fields):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    writer.append_pages_from_reader(reader)

    field_updates = {}
    for f in filled_fields:
        field_id = f.get("form_question_id")
        value = f.get("value")

        if field_id and value is not None:
            field_updates[field_id] = value

    writer.update_page_form_field_values(
        writer.pages,
        field_updates
    )

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Filled PDF saved to {output_path}")