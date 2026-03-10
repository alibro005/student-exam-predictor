from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.models.train_models import train_models


def run_pipeline():

    df = load_data("data/student_performance.csv")

    df = preprocess_data(df)

    X = df.drop(["exam_score", "student_id"], axis=1)
    y = df["exam_score"]

    train_models(X, y)