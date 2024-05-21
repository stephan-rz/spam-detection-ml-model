from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

# Load the model and vectorizer once at the start
vectorizer = load('tfidf_vectorizer.joblib')
model = load('spam_detection_model.joblib')

@app.post("/api/classify")
async def classify_message(message: Message):
    try:
        # Vectorize the message
        X = vectorizer.transform([message.message])

        # Predict using the model
        prediction = model.predict(X)

        # Convert prediction to a list for JSON serialization
        prediction_list = prediction.tolist()

        # Return the prediction
        if prediction_list[0] == 1:
            return  True
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3005)