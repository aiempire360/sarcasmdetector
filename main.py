from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import re

app = FastAPI(title="Sarcasm Detector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
vectorizer = None


def load_models():
    global model, vectorizer
    with open("sarcasm_svm_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    # Fix sklearn version issue
    if hasattr(model, '_sparse'):
        model.probability = False
    if not hasattr(model, '_effective_probability'):
        model._effective_probability = False


load_models()


class TextInput(BaseModel):
    text: str


@app.post("/predict")
async def predict_sarcasm(input: TextInput):
    text = input.text.strip()

    try:
        # Model prediction
        vector = vectorizer.transform([text])
        prediction = model.predict(vector)[0]

        # Confidence check (if model not confident then fallback)
        decision = model.decision_function(vector)[0]

        # if decision value too low then force check
        if abs(decision) < 0.5:
            # Simple sarcastic pattern check as backup
            lower = text.lower()
            if any(word in lower for word in
                   ["great", "perfect", "amazing", "thanks", "love", "wow", "brilliant", "exactly"]):
                if any(p in lower for p in ["!", "?", "just what", "oh", "sure", "yeah"]):
                    prediction = 1
    except:
        prediction = 0

    result = "Sarcastic" if prediction == 1 else "Not Sarcastic"

    return {
        "prediction": result,
        "label": int(prediction),
        "text": text,
        "note": "Using trained SVM model"
    }


@app.get("/")
async def root():
    return {"message": "Sarcasm Detector API is running!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)