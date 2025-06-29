# 🧠 AI Resume Analyzer (Django-based)

A smart resume analysis and matching tool built with **Python**, **Django**, and **Natural Language Processing**, designed to:

- 📥 Extract skills, education, and years of experience from resumes (PDF/DOCX)
- 🔍 Compare resumes to job descriptions using **TF-IDF + Cosine Similarity**
- 📊 Provide a match percentage and analysis summary
- 🛡️ Avoid `cryptography` issues by using **PyMuPDF** instead of pdfminer/pdfplumber

---

## 🚀 Features

- ✅ PDF and DOCX resume support
- ✅ Clean Django form interface
- ✅ Skill, education, and experience keyword matching
- ✅ Resume vs JD similarity scoring
- ✅ Lightweight and fast (no `cryptography` dependency)

---

## 📁 Project Structure

ai_resume_analyzer/
├── core/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── templates/
│ │ └── upload.html
├── media/ # Uploaded resume files
├── static/ # Static assets
├── db.sqlite3 # Default SQLite DB
├── manage.py
├── requirements.txt
└── README.md


## ⚙️ Installation

> 💡 Requires Python 3.8+ and `pip`.

```bash
git clone https://github.com/saugatpoudel100/resumeanalyzer.git
cd resumeanalyzer

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On macOS/Linux

# Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

📝 Running the App
e
# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
Visit: http://localhost:8000

🧠 How It Works
User uploads a resume (PDF or DOCX)

Resume text is extracted using:

PyMuPDF for PDFs

python-docx for DOCX

Text is processed with NLTK:

Tokenized

Stopwords removed

Keywords are matched:

Skills, Education, Years of Experience

Similarity Score is calculated using:

TF-IDF Vectorization

Cosine Similarity

📤 Upload Flow
Upload resume file (.pdf or .docx)

Paste job description text

View:

✅ Extracted Skills

🎓 Education matches

📆 Estimated Experience (in years)

📈 JD Match Percentage

🧪 NLTK Setup
In your code or Python shell, download required NLTK datasets (only once):

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Or run it manually in terminal:

bash
Copy code
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
💡 Screenshot (Optional)
Add an image like this in your repo and update the link:


🙌 Contributing
Pull requests are welcome! Feel free to fork this repo and improve the project.

📄 License
This project is open-source and licensed under the MIT License.

👤 Author
Developed with ❤️ by Saugat Paudel

GitHub: github.com/saugatpoudel100












