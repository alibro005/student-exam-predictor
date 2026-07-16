from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
  
    df = df.copy()

    df['sex'] = df['sex'].map({'M': 1, 'F': 0})
    df['schoolsup'] = df['schoolsup'].map({'yes': 1, 'no': 0})
    df['famsup'] = df['famsup'].map({'yes': 1, 'no': 0})
    df['internet'] = df['internet'].map({'yes': 1, 'no': 0})

    return df