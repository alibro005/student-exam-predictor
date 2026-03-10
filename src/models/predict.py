import joblib
import numpy as np

model = joblib.load("models/best_model.pkl")

def predict(features):

    features = np.array(features).reshape(1,-1)
    prediction = model.predict(features)

    return prediction[0]