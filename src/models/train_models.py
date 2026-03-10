import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_models(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "LinearRegression": LinearRegression(),
        "DecisionTree": DecisionTreeRegressor(),
        "RandomForest": RandomForestRegressor(n_estimators=200)
    }

    best_model = None
    best_score = -1

    for name, model in models.items():

        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = r2_score(y_test, preds)

        print(f"{name} R2 Score:", round(score,3))

        if score > best_score:
            best_score = score
            best_model = model

    joblib.dump(best_model, "models/best_model.pkl")

    print("Best model saved")
    