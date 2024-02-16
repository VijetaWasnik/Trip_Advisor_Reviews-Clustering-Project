import pandas as pd
from gensim.models import Word2Vec
import numpy as np

def document_vector(word2vec_model, doc):
    doc_vectors = [word2vec_model.wv[word] for word in doc if word in word2vec_model.wv.key_to_index]
    if len(doc_vectors) != 0:
        return np.mean(doc_vectors, axis=0)
    else:
        return np.zeros(word2vec_model.vector_size)

def train_word2vec_model(tokenized_data):
    word2vec_model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=1, workers=4)
    X_word2vec = np.array([document_vector(word2vec_model, doc) for doc in tokenized_data if document_vector(word2vec_model, doc) is not None])
    return word2vec_model, X_word2vec

