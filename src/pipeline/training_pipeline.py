from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.models.train_models import train_models


def run_pipeline():

    df = load_data("data/student_performance.csv")

    df = preprocess_data(df)

    X = df[
        [
            'sex',
            'age',
            'studytime',
            'failures',
            'schoolsup',
            'famsup',
            'internet',
            'health',
            'absences',
            'freetime',
            'goout',
            'G1',
            'G2'
        ]
    ]
    y = df["G3"]

    train_models(X, y)
