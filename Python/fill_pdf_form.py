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


def autofill_pdf(pdf, fields, output_path):
    for f in fields:
        page = pdf[f["page_num"]]
        rect = f["rect"]

        if f["field_type"] == '2':
            x = rect.x0
            y = rect.y0 + 8
            page.insert_text(
                (x, y),
                "x",
                fontsize=10,
                color=(0, 0, 0)
            )
        else:
            x = rect.x0
            y = rect.y0 + 8
            page.insert_text(
                (x, y),
                f"TEST: {f['field_name']}",
                fontsize=8,
                color=(0, 0, 0)
            )

    pdf.save(output_path)
    print(f"PDF saved as {output_path}")