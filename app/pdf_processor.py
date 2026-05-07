from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    documents = []

    for page_num, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            documents.append({
                "page": page_num + 1,
                "text": text
            })

    return documents