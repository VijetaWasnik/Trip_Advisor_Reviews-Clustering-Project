import pandas as pd
from data_preprocessing import preprocess_data
from model_training import train_word2vec_model, document_vector
from prediction import predict_clusters
from gensim.models import Word2Vec
import numpy as np
import pickle
from data_preprocessing import preprocess_data, clean_text
from model_training import document_vector, train_word2vec_model
from prediction import predict_clusters

def main():
    # Load preprocessed data
    df = preprocess_data("C:\\Users\\A\\Desktop\\Intrrvu\\capstone project - clustering\\New_Delhi_reviews1.csv")
    
    # Save preprocessed data
    df.to_csv('cleaned_review.csv', index=False)
    
    # Tokenize data
    tokenized_data = [review.split() for review in df['cleaned_review']]

    df = clean_text(df['cleaned_review'])
    
    # Train Word2Vec model
    word2vec_model, X_word2vec = train_word2vec_model(tokenized_data)
    
    # Save Word2Vec model
    with open("word2vec_model.pkl", "wb") as f:
        pickle.dump(word2vec_model, f)
    
    # Make predictions
    kmeans_labels = predict_clusters(X_word2vec)
    
    # Create a DataFrame with cluster labels
    clustered_data = pd.DataFrame({'rating_review': df['rating_review'],
                                   'review_full': df['review_full'],
                                   'cleaned_review': df['cleaned_review'],
                                   'cluster_label': kmeans_labels})
    
    # Save clustered data
    clustered_data.to_csv('clustered_data.csv', index=False)

if __name__ == "__main__":
    main()
