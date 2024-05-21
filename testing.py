import pandas as pd
from joblib import load

# Load the test dataset
test_file_path = 'test.csv'
test_df = pd.read_csv(test_file_path)

# Load the model and vectorizer
model = load('spam_detection_model.joblib')
vectorizer = load('tfidf_vectorizer.joblib')

# Vectorize the test messages
X_test = vectorizer.transform(test_df['message'])

# Predict
predictions = model.predict(X_test)

# Add predictions to the test dataframe
test_df['predicted_label'] = predictions
test_df['predicted_label'] = test_df['predicted_label'].map({0: 'ham', 1: 'spam'})

# Save the results to a new CSV file
result_file_path = 'test_spam_results.csv'
test_df.to_csv(result_file_path, index=False)

print("Predictions saved to:", result_file_path)










# import pandas as pd
# from joblib import load

# # Function to classify a single message
# def classify_message(message):
#     # Load the model and vectorizer
#     model = load('spam_detection_model.joblib')
#     vectorizer = load('tfidf_vectorizer.joblib')

#     # Vectorize the input message
#     X = vectorizer.transform([message])

#     # Predict
#     prediction = model.predict(X)
#     predicted_label = 'spam' if prediction[0] == 1 else 'ham'
    
#     return predicted_label


# message = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim now."
# predicted_label = classify_message(message)

# print(f"The message: '{message}' is classified as '{predicted_label}'")
