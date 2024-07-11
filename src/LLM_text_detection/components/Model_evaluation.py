import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from tensorflow.keras.models import load_model
from LLM_text_detection import logger
from LLM_text_detection.config.configuration import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval(self, X_test, y_test):
        # Load the model from the specified path
        model = load_model(self.config.model_path)
        # Evaluate the model on the test set
        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        print(f'Test Accuracy: {test_accuracy:.4f}')

        # Predict probabilities for the test set
        y_pred_prob = model.predict(X_test)

        # Convert probabilities to binary predictions (0 or 1)
        y_pred = (y_pred_prob > 0.5).astype(int)

        # Calculate and print classification report
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        # Calculate ROC-AUC score
        roc_auc = roc_auc_score(y_test, y_pred_prob)
        print(f"ROC-AUC Score: {roc_auc:.4f}")

        # Plotting the classification report as a heatmap
        report = classification_report(y_test, y_pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        plt.figure(figsize=(8, 6))
        sns.heatmap(report_df.iloc[:-1, :].astype(float), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Classification Report')
        plt.xlabel('Metrics')
        plt.ylabel('Classes')
        plt.show()

        # Calculate the confusion matrix
        conf_matrix = confusion_matrix(y_test, y_pred)

        # Plotting the confusion matrix as a heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted Labels')
        plt.ylabel('True Labels')
        plt.show()
