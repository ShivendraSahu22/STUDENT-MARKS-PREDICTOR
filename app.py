from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
#from schema.prediction_response import PredictionResponse
from model.predict import predict_marks, model, MODEL_VERSION



app = FastAPI()

# human readable       
@app.get('/')
def home():
    return {'message':'Student Marks Predictor API'}

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post('/predict', response_model=PredictionResponse)
def predict(data: UserInput):

    user_input = {
        'number_courses': data.number_courses,
        'time_study': data.time_study,
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))