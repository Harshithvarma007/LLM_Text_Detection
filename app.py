import streamlit as st
import pickle
from tensorflow.keras.models import load_model
import numpy as np

# Load the TF-IDF tokenizer
with open('assets/tfidf_tokenizer.pkl', 'rb') as f:
    tfidf_tokenizer = pickle.load(f)

# Load the trained model
loaded_model = load_model('assets/text_classification_model.h5')

# Function to preprocess text and make predictions
def predict_outcome(text):
    # Preprocess the text using the loaded tokenizer
    text_features = tfidf_tokenizer.transform([text])
    
    # Make predictions using the loaded model
    predictions = loaded_model.predict(text_features)
    
    # Return the predicted outcome (1 for positive, 0 for negative)
    return int(np.round(predictions[0][0]))

# Example passages
example_passages = {
    "AI in Healthcare": """
    The use of artificial intelligence (AI) in healthcare has revolutionized the way medical professionals diagnose and treat patients. With advanced algorithms and machine learning techniques, AI can analyze vast amounts of medical data to identify patterns and predict outcomes, aiding in early diagnosis and personalized treatment plans. This technology holds great promise for improving patient outcomes and reducing healthcare costs.
    """,
    "Climate Change": """
    Climate change is one of the most pressing issues facing our planet today. The increasing levels of greenhouse gases in the atmosphere, primarily due to human activities such as burning fossil fuels and deforestation, are causing global temperatures to rise. This has led to more frequent and severe weather events, melting polar ice, and rising sea levels. Addressing climate change requires immediate and concerted efforts from governments, businesses, and individuals worldwide.
    """,
    "Remote Work": """
    The COVID-19 pandemic has accelerated the adoption of remote work across various industries. Many companies have realized the benefits of allowing employees to work from home, including increased productivity, reduced overhead costs, and improved work-life balance. However, remote work also presents challenges such as maintaining team cohesion, ensuring cybersecurity, and managing employee well-being. As remote work becomes more prevalent, organizations must find ways to address these challenges and support their remote workforce.
    """
}

# Streamlit app
def main():
    st.title("AI Text Detection App")
    
    # Dropdown for example passages
    st.subheader("Example Passages")
    example_choice = st.selectbox("Choose an example passage:", list(example_passages.keys()))
    if st.button("Try"):
        input_text = example_passages[example_choice]
        st.session_state['input_text'] = input_text
    
    # Input text from user
    input_text = st.text_area("Enter the text you want to classify:", value=st.session_state.get('input_text', ''))
    
    # Button to make prediction
    if st.button("Predict"):
        if input_text.strip() != "":
            predicted_label = predict_outcome(input_text)
            if predicted_label == 1:
                st.markdown("<span style='color:red'>AI Detected</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='color:green'>Human Written</span>", unsafe_allow_html=True)
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
