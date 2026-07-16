# Student Performance Predictor

A machine learning project that predicts a student's **final grade (G3)** using demographic, academic, and lifestyle-related features from the UCI Student Performance dataset. The project compares multiple regression algorithms and deploys the best-performing model with a Streamlit web application.

---

##  Overview

This project applies supervised machine learning techniques to predict students' final academic performance.

Three regression models were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The **Random Forest Regressor** achieved the best performance and was selected for deployment.

---

##  Dataset

**Source:** UCI Machine Learning Repository – Student Performance Dataset

**Target Variable**

* **G3** – Final Grade (0–20)

**Features Used**

| Feature   | Description                           |
| --------- | ------------------------------------- |
| sex       | Student gender                        |
| age       | Student age                           |
| studytime | Weekly study time                     |
| failures  | Number of previous class failures     |
| schoolsup | Extra educational support from school |
| famsup    | Educational support from family       |
| internet  | Internet access at home               |
| health    | Current health status (1–5)           |
| absences  | Number of school absences             |
| freetime  | Free time after school (1–5)          |
| goout     | Going out with friends (1–5)          |
| G1        | First period grade                    |
| G2        | Second period grade                   |

**Target**

* **G3 (Final Grade)**

---

##  Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── student-mat.csv
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   ├── experimentation.ipynb
│   └── images/
│
├── src/
│   ├── data/
│   ├── models/
│   └── pipeline/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

---

##  Getting Started

### Clone the Repository

```bash
git clone https://github.com/alibro005/student-performance-predictor.git

cd student-performance-predictor
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Train the Model

```bash
python main.py
```

The training pipeline will:

* Load the dataset
* Preprocess the data
* Train multiple regression models
* Evaluate model performance
* Save the best model in the `models/` directory

---

##  Run the Streamlit App

```bash
streamlit run app.py
```

The application allows users to enter student information and predicts the expected final grade (G3).

---

##  Machine Learning Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Comparison
8. Save Best Model
9. Streamlit Deployment

---

##  Model Performance

The following models were evaluated:

| Model                   |      MAE |     RMSE | R² Score |
| ----------------------- | -------: | -------: | -------: |
| Linear Regression       | **1.46** | **2.19** | **0.77** |
| Random Forest Regressor | **1.08** | **1.81** | **0.84** |
| Decision Tree Regressor | **1.28** | **2.49** | **0.70** |

**Best Model:** Random Forest Regressor

---

##  Visualizations

The project includes:

* Feature correlation analysis
* Actual vs Predicted plots
* Model comparison
* Feature importance (Random Forest)

---

## License

This project is licensed under the [MIT License](LICENSE).

---


*Muhammad Ali Siddiqui © 2026*


