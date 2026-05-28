import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def preprocessing(text):
    text=text.lower()
    text=text.translate(str.maketrans("","",string.punctuation))
    text=word_tokenize(text)
    stop_words=set(stopwords.words("english"))
    text=[word for word in text if word not in stop_words]
    lemmatizer=WordNetLemmatizer()
    text=[lemmatizer.lemmatize(word) for word in text]
    text="".join(text)
    return text
job_text=preprocessing(job_text)
resume_text=preprocessing(resume_text)
documents=[job_text,resume_text]
vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(documents)
similarity_score=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])
print("Similarity Score:",similarity_score[0][0])