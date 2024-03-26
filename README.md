<h1>Customer Review Clustering for Theme Identification</h1>
<p>The objective of this project is to utilize customer reviews from TripAdvisor to cluster and identify top themes of positive and negative feedback. This aids businesses in understanding customer preferences and improving service quality.</p>

<h3>Project Structure</h3>
<strong>- 'app.py':</strong> Main application file responsible for integrating data preprocessing, model training, and prediction functionalities.
<br>
<strong>- 'data_preprocessing.py':</strong> Module for cleaning and preprocessing raw text data, including tasks such as removing stopwords, punctuation, and special characters.
<br>
<strong>- 'model_training.py':</strong> Module for training the clustering model using techniques like TF-IDF feature extraction and K-means clustering.
<br>
<strong>- 'prediction.py':</strong> Module for applying the trained model to predict clusters for new or unseen reviews.

<h3>Data Sources</h3>
The dataset used for this project consists of customer reviews from TripAdvisor. With a total of 147,581 records/reviews, this dataset serves as the foundation for clustering and identifying themes within customer feedback.
<br>

<h3>Data Preprocessing and Model Training </h3>
Data preprocessing and model training are performed on the TripAdvisor dataset to prepare it for clustering. The preprocessing steps involve cleaning and transforming raw text data, including the removal of stopwords, punctuation, and special characters. Subsequently, the data is prepared for model training by applying techniques like TF-IDF feature extraction.
<br>

<h3>Clustering</h3>
The dataset, after preprocessing, is clustered into 15 distinct groups using the K-means clustering algorithm. Each cluster represents a theme or topic derived from the customer reviews. The Silhouette Coefficient is utilized as a metric to evaluate the quality of the clustering, ensuring that the clusters are well-separated and internally coherent.
<br>
<h3>Results and Visualizations</h3>
Visualizations such as bar charts, word clouds, or scatter plots are generated to illustrate the identified clusters and themes from customer reviews. These visualizations provide insights into the distribution of reviews across different themes and highlight the prevalent topics within the dataset.
<br>
<h3>Contributing</h3>
Contributions to the project are welcome! Feel free to submit bug fixes, feature requests, or improvements via pull requests.
<br>

<h3>License</h3>
This project is licensed under the MIT License.
<br>

<h3>Contact</h3>
For inquiries or collaboration, contact wasnik_vijeta@gmail.com .
