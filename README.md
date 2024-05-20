# Spam Detection Model

This repository contains a machine learning model for detecting spam messages. The model is built using Python, FastAPI, and Scikit-learn, and it can be integrated into web applications for real-time spam detection.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Training](#model-training)
- [Testing the Model](#testing-the-model)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/spam-detection-model.git
    cd spam-detection-model
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

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
curl -X POST "http://localhost:3005/api/classify" -H "Content-Type: application/json" -d '{"message": "Congratulations! You have won a $1000 gift card."}'
