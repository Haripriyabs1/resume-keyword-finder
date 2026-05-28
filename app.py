import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
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
documents=['job_text','resume_text']
vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(documents)
