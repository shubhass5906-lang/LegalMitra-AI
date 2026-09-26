import pymupdf


def extract_text(uploaded_file):
    pdf_bytes = uploaded_file.getvalue()

    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    if not text.strip():
        return "⚠️ No text could be extracted from this PDF."

    return text