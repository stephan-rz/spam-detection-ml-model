import sys
from joblib import load

# Load the model and vectorizer
model = load('spam_detection_model.joblib')

# Get the message from the command line arguments
message = sys.argv[1]

# Vectorize the message
X = model.named_steps['tfidf'].transform([message])

# Predict
prediction = model.named_steps['clf'].predict(X)

# Print the prediction (0 for ham, 1 for spam)
print(prediction[0])
