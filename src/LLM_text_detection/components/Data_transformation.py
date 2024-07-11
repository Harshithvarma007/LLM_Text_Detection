import os
from LLM_text_detection import logger
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from LLM_text_detection.config.configuration import *
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def Data_transformation(self):
        data = pd.read_csv(self.config.data_path)
        # Initialize the TF-IDF Vectorizer
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        logger.info("Vectorizer is loaded")       
        # Tokenize and create TF-IDF vectors for the 'text' column of the dataset
        tfidf_vectors = tfidf_vectorizer.fit_transform(data['text'])
        logger.info("Vectorizer Transformed Data")        
        # Convert TF-IDF vectors to a DataFrame for easy analysis
        tfidf_df = pd.DataFrame(tfidf_vectors.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
        logger.info("Vectorization is completed")
        # Split the data into training and testing sets
        X = tfidf_df.values  # Features (TF-IDF vectors)
        y = data['label'].values  # Target variable
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logger.info("Spliting of Data is Completed")        
        # Encode target labels (0 and 1) using LabelEncoder
        label_encoder = LabelEncoder()
        y_train_encoded = label_encoder.fit_transform(y_train)
        y_test_encoded = label_encoder.transform(y_test)
        logger.info("Label Encoder is Done")        
        # Save the transformed data to CSV files
        return [X_train, X_test, y_train_encoded, y_test_encoded]
        pd.DataFrame(X_train).to_csv(os.path.join(self.config.root_dir,'x_train.csv'), index=False)
        pd.DataFrame(X_test).to_csv(os.path.join(self.config.root_dir,'x_test.csv'), index=False)
        pd.DataFrame(y_train_encoded).to_csv(os.path.join(self.config.root_dir,'y_train_encoded.csv'), index=False)
        pd.DataFrame(y_test_encoded).to_csv(os.path.join(self.config.root_dir,'y_test_encoded.csv'), index=False)
