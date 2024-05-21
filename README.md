# Spam Detection Model

This repository contains a spam detection model built using scikit-learn and FastAPI. The model can classify messages as either "spam" or "ham" (not spam). The repository includes code for training the model, testing the model, and setting up an API for real-time spam detection.

## Contents

- `spam_model.ipynb`: Jupyter notebook for training the spam detection model.
- `testing.py`: Python script for testing the spam detection model on a dataset.
- `requirements.txt`: List of Python packages required for the project.
- `spam.csv`: The dataset used for training the model.
- `test.csv`: The dataset used for testing the model.

## Setup

1. Clone the repository

```bash
git clone https://github.com/yourusername/spam-detection-model.git
cd spam-detection-model
```
2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages
```bash
pip install -r requirements.txt
```

## Training the Model
To train the model, use the spam_model.ipynb Jupyter notebook. You can run the notebook locally or use a Jupyter notebook service like Google Colab.

## Testing the Model
To test the model, run the testing.py script:

```bash
python testing.py
```

# License
This project is licensed under the MIT License.

