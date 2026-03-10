from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    categorical_cols = ["gender", "academic_level", "internet_quality"]

    encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df