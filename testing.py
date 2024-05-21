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

