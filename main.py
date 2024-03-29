from fastapi import FastAPI, Depends
from prediction_endpoint import FraudDetector, PredictionOutput, PredictionInput

app = FastAPI()
fraud_model = FraudDetector()

# Define an endpoint for making predictions


@app.post("/prediction")
async def prediction(input_data: PredictionInput) -> PredictionOutput:
    # Call the predict method of FraudDetector with input_data
    output = fraud_model.predict(input_data)
    return output

# Define an event handler to load the model during startup


@app.on_event("startup")
async def startup():
    fraud_model.load_model()
