import pickle
import numpy as np

def load_model(model_name):
    path = f"models/{model_name}.pkl"
    with open(path, "rb") as file:
        model = pickle.load(file)
    return model

def make_predict(model_name, input_data):
    try:
        model = load_model(model_name)
        input_array = np.array([input_data])
        prediction = model.predict(input_array)
        return prediction[0]
    except Exception as e:
        return f"Error: {str(e)}"
    