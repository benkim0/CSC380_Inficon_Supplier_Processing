from pypdf import PdfReader, PdfWriter
import fitz

def extract_pdf_fields(pdf_path):
    pdf = fitz.open(pdf_path)
    fields = []

    for page_num, page in enumerate(pdf):
        if hasattr(page, "widgets") and page.widgets():
            for w in page.widgets():
                if not w.field_name:
                    continue
                fields.append({
                    "field_name": w.field_name,
                    "rect": w.rect,
                    "field_type": w.field_type.name if hasattr(w.field_type, "name") else str(w.field_type),
                    "page_num": page_num
                })

    if not fields:
        print("No fields found in this PDF")
    return fields, pdf


def autofill_pdf(input_pdf_path, output_pdf_path, match_results):
    pdf = fitz.open(input_pdf_path)

    for match in match_results:
        answer = match.get("answer")
        rect = match.get("rect")
        page_num = match.get("page_num", 0)

        if not answer or not rect:
            continue

        if rect.is_empty or rect.width == 0 or rect.height == 0:
            rect = fitz.Rect(rect.x0, rect.y0, rect.x0 + 100, rect.y0 + 20)

        if str(answer).lower() in ("yes", "true", "1"):
            text_to_insert = "✔"
        elif str(answer).lower() in ("no", "false", "0"):
            text_to_insert = "✗"
        else:
            text_to_insert = str(answer)

        pdf[page_num].insert_textbox(
            rect,
            text_to_insert,
            fontsize=11,
            fontname="helv",
            align=0,
            color=(0, 0, 0)
        )

    pdf.save(output_pdf_path)
    print(f"PDF saved as {output_pdf_path} (via text overlay)")