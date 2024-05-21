import pandas as pd
from joblib import load

# Function to classify a single message
def classify_message(message):
    # Load the model and vectorizer
    model = load('spam_detection_model.joblib')
    vectorizer = load('tfidf_vectorizer.joblib')

    # Vectorize the input message
    X = vectorizer.transform([message])

    # Predict
    prediction = model.predict(X)
    predicted_label = 'spam' if prediction[0] == 1 else 'ham'
    
    return predicted_label


message = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim now."
predicted_label = classify_message(message)

print(f"The message: '{message}' is classified as '{predicted_label}'")
