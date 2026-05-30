import string
import nltk
import streamlit as st
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
def preprocessing(text):
    text=text.lower()
    text=text.translate(str.maketrans("","",string.punctuation))
    text=word_tokenize(text)
    stop_words=set(stopwords.words("english"))
    text=[word for word in text if word not in stop_words]
    lemmatizer=WordNetLemmatizer()
    text=[lemmatizer.lemmatize(word) for word in text]
    text=" ".join(text)
    return text
st.markdown(
    """
    <h1 style='text-align: center;
    color: #4F46E5;
    font-size: 60px;'>
    ResumeFit
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center;
    color: gray;
    font-size: 22px;'>
    An AI-powered tool to match your resume with job descriptions
    </p>
    """,
    unsafe_allow_html=True
)
job_text=st.text_area("Enter the job description:")
resume=st.file_uploader("Upload your resume (PDF):", type=["pdf"])
resume_text = ""
if resume is not None:
    reader=PdfReader(resume)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text
if st.button("Calculate Similarity"):
    if not job_text:
        st.warning("Please enter a job description.")
    elif not resume:
        st.warning("Please upload your resume.") 
    else:
        with st.spinner("Analyzing resume..."):
            job_text=preprocessing(job_text)
            resume_text=preprocessing(resume_text)
            documents=[job_text,resume_text]
            vectorizer=TfidfVectorizer()
            tfidf_matrix=vectorizer.fit_transform(documents)
            similarity_score=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])
            score=similarity_score[0][0]*100
            st.write(f"Similarity Score: {score:.2f}%")
            if score>80:
                st.success("Great match! Your resume is well-aligned with the job description.")
            elif score>50:
                st.warning("Good match! Consider tailoring your resume more to the job description.")
            else:
                st.error("Poor match! Consider revising your resume to better fit the job description.")
            