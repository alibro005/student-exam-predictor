from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.models.train_models import train_models


def run_pipeline():

    df = load_data("data/student_performance.csv")

    df = preprocess_data(df)

    X = df[
        [
            "study_hours",
            "self_study_hours",
            "sleep_hours",
            "focus_index",
            "burnout_level",
            "productivity_score",
            "mental_health_score",
            "screen_time_hours",
            "social_media_hours",
            "gaming_hours",
        ]
    ]
    y = df["exam_score"]

    train_models(X, y)
