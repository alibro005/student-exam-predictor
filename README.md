#  Student Exam Score Predictor

A machine learning project that predicts student exam scores based on key academic and demographic factors. Built with Python and scikit-learn, this end-to-end notebook covers data exploration, model training, evaluation, and prediction.

---

##  Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Notebook](#running-the-notebook)
- [Workflow](#workflow)
- [Results](#results)
- [License](#license)

---

## Overview

This project predicts student exam performance using Random Forest Regression. By analyzing features such as study hours, self-study hours, sleep, focus, burnout, productivity, mental health, and screen/social/gaming time, the model helps identify performance patterns and allows predictions for new students.

---

##  Dataset

The dataset is stored in the `data/` directory and contains student-level records with features such as:

| Feature             | Description                          |
| ------------------- | ------------------------------------ |
| study_hours         | Average hours spent studying per day |
| self_study_hours    | Hours of self-study per day          |
| sleep_hours         | Average sleep hours per day          |
| focus_index         | Student’s focus level (0–1 scale)    |
| burnout_level       | Burnout level (0–1 scale)            |
| productivity_score  | Productivity score (0–100)           |
| mental_health_score | Mental health score (0–100)          |
| screen_time_hours   | Total screen time per day (hours)    |
| social_media_hours  | Hours spent on social media per day  |
| gaming_hours        | Hours spent on gaming per day        |
| exam_score          | Final exam score (target variable)   |

---

##  Project Structure

```
student-exam-predictor/
│
├── data/                          # Dataset files
│   └── sample_data.csv            # Raw student performance data
│
├── student_exam_predictor.ipynb   # Main Jupyter Notebook (ML pipeline)
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

---

##  Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Jupyter Notebook | Interactive development environment |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Matplotlib / Seaborn | Data visualization |
| Scikit-learn | Machine learning models and evaluation |

---

##  Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/alibro005/student-exam-predictor.git
cd student-exam-predictor
```

2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

### Running the Notebook

Launch Jupyter Notebook in the project directory:

```bash
jupyter notebook
```

Then open `student_exam_predictor.ipynb` from the Jupyter interface and run all cells sequentially.

---

##  Workflow

The notebook follows a structured ML pipeline:

1. **Data Loading** — Import and inspect the raw dataset
2. **Exploratory Data Analysis (EDA)** — Visualize distributions, correlations, and outliers
3. **Data Preprocessing** — Handle missing values, encode categorical variables, scale features
4. **Model Training** — Train regression models (e.g., Linear Regression, Random Forest)
5. **Model Evaluation** — Assess performance using metrics such as MAE, RMSE, and R²
6. **Prediction** — Generate exam score predictions on new/test data

---

##  Results

The trained model achieves strong predictive performance on the test set. Key metrics:

| Metric | Score |
|---|---|
| R² Score | *See notebook* |
| Mean Absolute Error (MAE) | *See notebook* |
| Root Mean Squared Error (RMSE) | *See notebook* |

> Metrics are calculated on the test set.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
