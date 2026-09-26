\# ⚖️ LegalMitra AI



\### AI-Powered Legal Document Simplifier for Indian Languages



LegalMitra AI is an AI-powered application that helps users understand legal documents in simple language.



Users can upload a PDF legal document, select an Indian language, and generate an easy-to-understand explanation using Google Gemini AI.



\## 🌐 Supported Languages



\* English

\* Kannada

\* Hindi

\* Telugu

\* Tamil

\* Malayalam

\* Marathi

\* Bengali



\## ✨ Features



\* 📄 Upload legal PDF documents

\* 🔍 Extract text from PDF files

\* 🤖 AI-powered document explanation using Google Gemini

\* 🌐 Explanation in 8 Indian languages

\* 📌 Identifies important information such as:



&#x20; \* People or parties involved

&#x20; \* Main purpose

&#x20; \* Important dates

&#x20; \* Money or amounts

&#x20; \* Conditions

&#x20; \* Responsibilities

&#x20; \* Important points

\* 👨‍👩‍👧 Designed to make complex legal documents easier for ordinary people to understand



\## 🛠️ Technologies Used



\* Python

\* Streamlit

\* Google Gemini API

\* PyMuPDF

\* Python-dotenv



\## 📂 Project Structure



```text

LegalMitra-AI/

│

├── app.py

├── utils/

│   └── pdf\_reader.py

├── .gitignore

├── README.md

└── requirements.txt

```



\## 🚀 How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/shubhass5906-lang/LegalMitra-AI.git

```



\### 2. Open the project



```bash

cd LegalMitra-AI

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



Windows:



```bash

venv\\Scripts\\activate

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\### 6. Create `.env`



Create a file named:



```text

.env

```



Add your own Gemini API key:



```text

GEMINI\_API\_KEY=your\_api\_key\_here

```



Never upload your `.env` file or API key to GitHub.



\### 7. Run the application



```bash

streamlit run app.py

```



\## ⚠️ Disclaimer



LegalMitra AI is an educational tool designed to simplify legal documents for easier understanding.



It does not provide legal advice and does not replace a qualified legal professional.



Users should verify important legal matters with an appropriate legal professional.



\## 🎯 Future Improvements



\* OCR support for scanned legal documents

\* Voice-based explanation

\* More Indian languages

\* Important clause detection

\* Automatic extraction of dates and amounts

\* Improved document privacy

\* Deployment as a web application



\## 👩‍💻 Project



\*\*LegalMitra AI\*\*



Built using Python, Streamlit and Google Gemini AI.



