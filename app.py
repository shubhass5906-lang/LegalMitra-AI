import os
import streamlit as st
import pymupdf
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None


# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="LegalMitra AI",
    page_icon="⚖️",
    layout="wide"
)


# -----------------------------
# TITLE
# -----------------------------

st.title("⚖️ LegalMitra AI")

st.write(
    "Upload a legal document and get a simple explanation "
    "that is easy for everyone to understand."
)

st.info(
    "⚠️ LegalMitra AI provides a simplified explanation "
    "for understanding. It is not legal advice."
)


# -----------------------------
# LANGUAGE SELECTION
# -----------------------------

languages = [
    "English",
    "ಕನ್ನಡ",
    "हिन्दी",
    "తెలుగు",
    "தமிழ்",
    "മലയാളം",
    "मराठी",
    "বাংলা"
]

language = st.selectbox(
    "🌐 Choose your language",
    languages
)


# -----------------------------
# PDF UPLOAD
# -----------------------------

st.subheader("📄 Upload your legal document")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


# -----------------------------
# PROCESS PDF
# -----------------------------

if uploaded_file is not None:

    st.success("✅ Document uploaded successfully!")

    st.write(
        "File name:",
        uploaded_file.name
    )

    # Read PDF
    pdf_bytes = uploaded_file.getvalue()

    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()


    # -----------------------------
    # DOCUMENT TEXT
    # -----------------------------

    st.subheader("📖 Document Text")

    if text.strip():

        st.success(
            f"✅ Text extracted successfully! "
            f"Characters: {len(text)}"
        )

        with st.expander("View extracted document text"):

            st.text_area(
                "Document text",
                text,
                height=300
            )

    else:

        st.warning(
            "⚠️ No text could be extracted from this PDF."
        )


    # -----------------------------
    # AI SUMMARY
    # -----------------------------

    st.subheader("🤖 Simple Legal Explanation")

    st.write(
        f"Selected language: **{language}**"
    )


    if st.button(
        "✨ Generate Simple Explanation",
        use_container_width=True
    ):

        if not GEMINI_API_KEY:

            st.error(
                "❌ Gemini API key was not found. "
                "Please check your .env file."
            )

        elif not text.strip():

            st.warning(
                "⚠️ No document text is available."
            )

        else:

            with st.spinner(
                "🤖 Gemini is analyzing the document..."
            ):

                try:

                    prompt = f"""
You are LegalMitra AI.

Your job is to explain a legal document in very simple language
so that a parent or ordinary person can understand it.

IMPORTANT RULES:

1. Use ONLY information found in the document.
2. Do NOT invent facts.
3. Do NOT provide legal advice.
4. If information is missing, write:
   "Not mentioned in the document."
5. Explain difficult legal terms in simple language.
6. Keep the explanation clear and easy to read.
7. Write the complete explanation in this language:
   {language}

Use these sections:

📄 1. What is this document?

👥 2. People or parties involved

🎯 3. Main purpose of the document

📅 4. Important dates

💰 5. Money or amounts mentioned

📌 6. Important conditions

📝 7. Responsibilities of each party

⚠️ 8. Important things to notice

💡 9. Simple overall explanation

DOCUMENT:

{text}
"""

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=prompt
                    )

                    summary = response.text

                    st.success(
                        "✅ Explanation generated successfully!"
                    )

                    st.markdown(summary)


                except Exception as e:

                    st.error(
                        "❌ Gemini could not generate the explanation."
                    )

                    st.write(
                        str(e)
                    )


# -----------------------------
# DISCLAIMER
# -----------------------------

st.divider()

st.caption(
    "⚖️ LegalMitra AI is an educational tool for simplifying "
    "legal documents. It does not replace professional legal advice."
)