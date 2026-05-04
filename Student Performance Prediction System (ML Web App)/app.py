# ================================
# 🎓 Student Grade Predictor App
# Portfolio-Ready Version (Day 71)
# ================================

# 1️⃣ Import Required Libraries
import streamlit as st
import pickle
import numpy as np

# 2️⃣ Page Configuration
st.set_page_config(
    page_title="Student Grade Predictor",
    page_icon="🎓",
    layout="wide"
)

# 3️⃣ Load Trained Model (Make sure grade_model.pkl is in same folder)
@st.cache_resource
def load_model():
    with open("grade_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# 4️⃣ App Title & Description
st.title("🎓 Student Grade Predictor")
st.subheader("AI-powered Grade Prediction System")
st.info("Enter student marks from the sidebar and click Predict.")

st.markdown("---")

# 5️⃣ Sidebar Input Section
st.sidebar.header("📥 Input Section")

marks = st.sidebar.slider(
    "Enter Student Marks",
    min_value=0,
    max_value=100,
    value=50
)

subject = st.sidebar.selectbox(
    "Select Subject",
    ["Mathematics", "Science", "English"]
)

# 6️⃣ Initialize Prediction History
if "history" not in st.session_state:
    st.session_state.history = []

# 7️⃣ Layout Columns
col1, col2 = st.columns(2)

with col1:
    st.write("### 📊 Input Summary")
    st.write(f"**Subject:** {subject}")
    st.write(f"**Marks Entered:** {marks}")

with col2:
    st.write("### 🎯 Prediction Result")

# 8️⃣ Prediction Button Logic
if st.button("🚀 Predict Grade"):

    # Input validation
    if marks < 0 or marks > 100:
        st.error("Marks must be between 0 and 100.")
    else:
        # Format input properly for model
        input_data = np.array([[marks]])

        # Model Prediction
        prediction = model.predict(input_data)[0]

        # Store in history
        st.session_state.history.append((subject, marks, prediction))

        # Styled Output
        if prediction == "A":
            st.success(f"Excellent Performance in {subject}! 🎉 Grade: {prediction}")
        elif prediction == "B":
            st.info(f"Good Performance in {subject}! 👍 Grade: {prediction}")
        else:
            st.warning(f"Needs Improvement in {subject}. ⚠️ Grade: {prediction}")

st.markdown("---")

# 9️⃣ Prediction History Section
if st.session_state.history:
    st.write("### 📜 Prediction History")
    st.table(
        st.session_state.history
    )

# 🔟 Reset History Button
if st.button("🗑 Reset History"):
    st.session_state.history = []
    st.success("Prediction history cleared successfully.")

st.markdown("---")

# 1️⃣1️⃣ Expandable Model Explanation
with st.expander("ℹ️ How does this model work?"):
    st.write("""
    This Machine Learning model predicts student grades based on input marks.
    The model was trained on historical student performance data and deployed
    using Streamlit for interactive web-based predictions.
    """)

# ================================
# ✅ End of App
# ================================