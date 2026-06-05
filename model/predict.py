import pickle

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# MLFlow
MODEL_VERSION = '1.0.0'

def predict_marks(user_input):
    # Convert user input to a format suitable for prediction
    input_data = [[user_input.number_courses, user_input.time_study]]
    
    # Make prediction using the loaded model
    predicted_marks = model.predict(input_data)
    
    return predicted_marks[0]
