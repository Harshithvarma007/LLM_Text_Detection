import pandas as pd
import os
from  LLM_text_detection import logger
import pickle
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from LLM_text_detection.config.configuration import *
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self,res):
        # Load the training and testing data from the CSV files using self.config
        X_train = res[0]
        X_test = res[1]
        y_train_encoded = res[2]
        y_test_encoded = res[3]
        logger.info("Data Loaded")
        # Build a simple neural network model
        model = Sequential([
            Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
            Dropout(0.3),
            Dense(64, activation='relu'),
            Dropout(0.3),
            Dense(1, activation='sigmoid')
        ])
  
        # Compile the model
        model.compile(optimizer=Adam(learning_rate=self.config.learning_rate),
                    loss=self.config.loss,
                    metrics=self.config.metrics)
        logger.info("Model Compiled")              
        
        # Train the model
        history = model.fit(X_train, y_train_encoded,
                            epochs=10,
                            batch_size=32,
                            validation_data=(X_test, y_test_encoded),
                            verbose=1)
        logger.info("Model training Completed")              
        # Save the model
        model.save(os.path.join(self.config.root_dir, self.config.model_name))
        logger.info("Model Saved")      
        return history  