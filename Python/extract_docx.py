from docx2python import docx2python

def extract_docx_questions(filepath):
    doc = docx2python(filepath)

    full_text = doc.text

    lines = [line.strip() for line in full_text.split("\n") if line.strip()]

    return lines

def clean_lines(lines):
    seen = set()
    cleaned = []
    for line in lines:
        line = line.strip()
        if line and line not in seen:
            cleaned.append(line)
            seen.add(line)
    return cleaned