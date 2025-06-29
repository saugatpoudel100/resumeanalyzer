from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume

import nltk
import re
import docx
import fitz  # PyMuPDF

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (only once)
nltk.download('punkt')
nltk.download('stopwords')

# Define keywords
SKILLS_KEYWORDS = {
    'python', 'java', 'c++', 'javascript', 'django', 'flask', 'react', 'node',
    'machine learning', 'data analysis', 'nlp', 'sql', 'aws', 'docker', 'kubernetes'
}
EDUCATION_KEYWORDS = {
    'bachelor', 'master', 'phd', 'b.sc', 'm.sc', 'bs', 'ms', 'university', 'college'
}
EXPERIENCE_PATTERN = re.compile(r'(\d+(\.\d+)?)\s+(years?|yrs?)', re.IGNORECASE)

def extract_text(file):
    filename = file.name.lower()
    
    if filename.endswith('.pdf'):
        # Use PyMuPDF for PDF text extraction
        # file.read() returns bytes, so use stream=True in fitz.open
        file_bytes = file.read()
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
        return text
    
    elif filename.endswith('.docx'):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    
    else:
        try:
            return file.read().decode('utf-8')
        except UnicodeDecodeError:
            file.seek(0)
            return file.read().decode('latin1')

def analyze_resume(text):
    text_lower = text.lower()
    words = set(word_tokenize(text_lower))
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if w.isalpha() and w not in stop_words]

    skills_found = []
    for skill in SKILLS_KEYWORDS:
        if ' ' in skill:  # multi-word skill
            if skill in text_lower:
                skills_found.append(skill)
        else:
            if skill in filtered_words:
                skills_found.append(skill)

    education_found = [edu for edu in EDUCATION_KEYWORDS if edu in text_lower]
    experience_years = sum(float(match[0]) for match in EXPERIENCE_PATTERN.findall(text))

    return {
        'skills': skills_found,
        'education': education_found,
        'experience_years': experience_years,
    }

def score_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([jd_text, resume_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity * 100, 2)

def upload_resume(request):
    analysis = None
    match_percentage = None

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_instance = form.save()
            file = resume_instance.resume_file
            jd_text = form.cleaned_data.get('job_description', '')

            text = extract_text(file)
            analysis = analyze_resume(text)

            if jd_text:
                match_percentage = score_similarity(text, jd_text)
    else:
        form = ResumeForm()

    return render(request, 'upload.html', {
        'form': form,
        'analysis': analysis,
        'match_percentage': match_percentage,
    })  