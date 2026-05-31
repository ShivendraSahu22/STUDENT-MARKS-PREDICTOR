from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# human readable       
@app.get('/')
def home():
    return {'message':'Student Marks Predictor API'}



@app.post('/predict', response_model=PredictionResponse)
def predict(user_input: UserInput):