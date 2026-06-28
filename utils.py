import re
import pdfplumber


def clean_text(text):

    if not isinstance(text, str):
        text = str(text)

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        text
    )

    return text


def extract_resume_text(uploaded_file):

    text = ""

    with pdfplumber.open(
        uploaded_file
    ) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text