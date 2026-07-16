import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor", page_icon="🎓", layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/best_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Performance Predictor")

st.markdown("""
Predict a student's **Final Grade (G3)** using demographic information,
study habits, and previous academic performance.
""")

st.divider()

# ==================================
# Student Information
# ==================================

st.header("👤 Student Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])

with col2:
    age = st.slider("Age", 15, 22, 17)

# ==================================
# Academic Information
# ==================================

st.header("📚 Academic Information")

studytime = st.selectbox(
    "Weekly Study Time",
    options=[1, 2, 3, 4],
    help="""
1 = Less than 2 hours/week

2 = 2 to 5 hours/week

3 = 5 to 10 hours/week

4 = More than 10 hours/week
""",
)

failures = st.slider("Previous Class Failures", 0, 4, 0)

col1, col2 = st.columns(2)

with col1:
    schoolsup = st.selectbox("School Educational Support", ["Yes", "No"])

with col2:
    famsup = st.selectbox("Family Educational Support", ["Yes", "No"])

internet = st.selectbox("Internet Access at Home", ["Yes", "No"])

health = st.slider("Health Status", 1, 5, 3, help="1 = Very Poor | 5 = Excellent")

absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=5)

col1, col2 = st.columns(2)

with col1:
    freetime = st.slider("Free Time After School", 1, 5, 3)

with col2:
    goout = st.slider("Going Out With Friends", 1, 5, 3)

# ==================================
# Previous Performance
# ==================================

st.header("📈 Previous Academic Performance")

st.info("These are the student's grades before the final examination.")

col1, col2 = st.columns(2)

with col1:
    g1 = st.slider("First Period Grade (G1)", 0, 20, 10)

with col2:
    g2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

st.divider()

# ==================================
# Prediction
# ==================================

if st.button("🎯 Predict Final Grade", use_container_width=True):

    # Encode categorical values
    gender = 1 if gender == "Male" else 0
    schoolsup = 1 if schoolsup == "Yes" else 0
    famsup = 1 if famsup == "Yes" else 0
    internet = 1 if internet == "Yes" else 0

    input_data = np.array(
        [
            [
                gender,
                age,
                studytime,
                failures,
                schoolsup,
                famsup,
                internet,
                health,
                absences,
                freetime,
                goout,
                g1,
                g2,
            ]
        ]
    )

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(20, prediction))

    percentage = (prediction / 20) * 100

    st.success(f"### 🎓 Predicted Final Grade: **{prediction:.2f} / 20**")

    st.progress(int(percentage))

    st.write(f"### Percentage: **{percentage:.1f}%**")

    # Performance Category
    if prediction >= 16:
        st.success("🏆 Performance: Excellent")

    elif prediction >= 14:
        st.success("🥇 Performance: Very Good")

    elif prediction >= 10:
        st.info("👍 Performance: Good")

    elif prediction >= 8:
        st.warning("⚠️ Performance: Average")

    else:
        st.error("❌ Performance: Needs Improvement")
