# Spam Detection Model

This repository contains a machine learning model for detecting spam messages. The model is built using Python, FastAPI, and Scikit-learn, and it can be integrated into web applications for real-time spam detection.

## Table of Contents

- [Spam Detection Model](#spam-detection-model)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Clone the Repository](#clone-the-repository)
    - [Common Method](#common-method)
    - [Docker Method](#docker-method)
  - [Usage](#usage)
    - [Running the FastAPI Server](#running-the-fastapi-server)
    - [Example Request](#example-request)
  - [API Endpoints](#api-endpoints)
    - [POST /api/classify](#post-apiclassify)
  - [Model Training](#model-training)
  - [Testing the Model](#testing-the-model)
  - [Contributors](#contributors)

## Installation
### Clone the Repository

1. Clone the repository:
    ```bash
    git clone https://github.com/stephan-rz/spam-detection-ml-model.git
    cd spam-detection-ml-model
    ```
### Common Method

1. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
### Docker Method
1. Build the Docker image:
    ```bash
    docker build -t spam-detection-model .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 3005:3005 spam-detection-model
    ```
    The server will be running at `http://localhost:3005`.

## Usage

### Running the FastAPI Server

1. Start the FastAPI server:
    ```bash
    uvicorn server:app --reload --host 0.0.0.0 --port 3005
    ```

2. The server will be running at `http://localhost:3005`. You can use tools like `curl`, `Postman`, or a web browser to interact with the API.

### Example Request

Send a POST request to classify a message:
```bash
curl -X POST "http://localhost:3005/api/classify" -H "Content-Type: application/json" -d '{"message": "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward!,"}'
```
The response will be:

```bash
true
```

## API Endpoints

### POST /api/classify

Description: Classify a message as spam or ham.

Request Body:
```bash
{
    "message": "string"
}
```

Response:
```bash
boolean
```

## Model Training


To train the model, use the provided script:

```bash
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from joblib import dump

# Load your dataset
file_path = 'path/to/your/spam.csv'
data = pd.read_csv(file_path, encoding='latin1')

# Keep only the relevant columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Encode the labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split into features and labels
X = data['message']
y = data['label']

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
dump(model, 'spam_detection_model.joblib')
dump(vectorizer, 'tfidf_vectorizer.joblib')

```

## Testing the Model

To test the model on new messages:

```bash
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

# Example usage
message = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim now."
predicted_label = classify_message(message)

print(f"The message: '{message}' is classified as '{predicted_label}'")

```

## Contributors

- **Student Name - D.S.C. Wijesuriya | Reg Number -  IT21155802**
- **Student Name - W.N. Dilsara | Reg Number -  IT21182600**

<a href="https://github.com/stephan-rz/spam-detection-ml-model/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=stephan-rz/spam-detection-ml-model" />
</a>

