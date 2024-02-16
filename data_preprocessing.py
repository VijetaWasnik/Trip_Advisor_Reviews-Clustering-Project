import pandas as pd
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in set(stopwords.words('english'))])
    return text

def preprocess_data(file):
    df = pd.read_csv(file)
    df = df.dropna()
    df['cleaned_review'] = df['review_full'].apply(clean_text)
    return df

