import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="OncoPredict AI",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.hero {
    background: linear-gradient(135deg,#0f172a,#0f766e,#0891b2);
    padding: 40px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}
.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 18px;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}
.section-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.ai-box {
    background: linear-gradient(135deg,#dbeafe,#f0fdf4);
    padding: 20px;
    border-radius: 18px;
    border-left: 6px solid #0ea5e9;
}
.workflow-box {
    background: linear-gradient(135deg,#ecfeff,#f0fdf4);
    padding: 20px;
    border-radius: 18px;
    border-left: 6px solid #10b981;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("logo.png", width=180)
st.sidebar.title("OncoPredict AI")

st.sidebar.markdown("""
### Platform Features
✅ AI Risk Prediction  
✅ Workflow Automation  
✅ BMI Analytics  
✅ Smart Recommendations  
✅ Visual Dashboard  
✅ Downloadable Reports  
""")

st.sidebar.info(
    "Educational healthcare prototype for AI-assisted cancer risk awareness and prevention support."
)

# Hero
st.markdown("""
<div class="hero">
    <h1>🩺 OncoPredict AI</h1>
    <p>AI-Based Cancer Risk Prediction & Prevention Support System</p>
</div>
""", unsafe_allow_html=True)
st.warning(
    "Disclaimer: This application is developed for educational and awareness purposes only and does not provide medical diagnosis."
)

st.warning(
    "Disclaimer: This application is developed for educational and awareness purposes only and does not provide medical diagnosis."
)

# Inputs
st.markdown("## 👤 Patient Health Assessment")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    age = st.slider("Age", 10, 100, 30)
    weight = st.number_input("Weight (kg)", 20, 200, 65)
    height = st.number_input("Height (cm)", 100, 250, 170)
    smoking = st.selectbox(
        "Smoking Habit",
        ["Non-Smoker", "Occasional Smoker", "Regular Smoker"]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    family_history = st.selectbox("Family History of Cancer", ["No", "Yes"])
    exercise = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
    alcohol = st.selectbox("Alcohol Consumption", ["No", "Occasionally", "Frequently"])
    stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
    st.markdown('</div>', unsafe_allow_html=True)

# BMI
height_m = height / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

# Risk logic
risk_score = 0

if age > 50:
    risk_score += 2

if smoking == "Occasional Smoker":
    risk_score += 1
elif smoking == "Regular Smoker":
    risk_score += 3

if family_history == "Yes":
    risk_score += 3

if exercise == "Low":
    risk_score += 2

if alcohol == "Frequently":
    risk_score += 2

if bmi >= 30:
    risk_score += 2

if stress == "High":
    risk_score += 2

# Dashboard
st.markdown("## 📊 AI Healthcare Dashboard")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>BMI</h3>
        <h2>{bmi:.2f}</h2>
        <p>{bmi_status}</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Risk Score</h3>
        <h2>{risk_score}/16</h2>
        <p>AI Evaluation</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <h3>Automation</h3>
        <h2>Enabled</h2>
        <p>Workflow Active</p>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <h3>AI Engine</h3>
        <h2>Active</h2>
        <p>Smart Analysis</p>
    </div>
    """, unsafe_allow_html=True)

# Risk prediction
st.markdown("## 🧠 AI Risk Prediction")

progress_value = min(risk_score / 16, 1.0)
st.progress(progress_value)

if risk_score >= 10:
    risk_level = "High Risk"
    st.error("🔴 High Cancer Risk")
elif risk_score >= 5:
    risk_level = "Moderate Risk"
    st.warning("🟠 Moderate Cancer Risk")
else:
    risk_level = "Low Risk"
    st.success("🟢 Low Cancer Risk")

# Recommendations
st.markdown("""
<div class="ai-box">
<h3>🤖 AI-Generated Prevention Recommendations</h3>
</div>
""", unsafe_allow_html=True)

recommendations = []

if smoking == "Regular Smoker":
    recommendations.append("⚠ Smoking cessation is strongly recommended.")

if smoking == "Occasional Smoker":
    recommendations.append("⚠ Reducing smoking exposure is recommended.")

if bmi >= 30:
    recommendations.append("⚠ Weight management and dietary improvement are advised.")

if exercise == "Low":
    recommendations.append("💪 Increasing physical activity may reduce long-term health risks.")

if family_history == "Yes":
    recommendations.append("🩺 Regular screening is recommended due to family history.")

if alcohol == "Frequently":
    recommendations.append("🍷 Reducing alcohol intake is recommended.")

if stress == "High":
    recommendations.append("🧘 Stress management strategies are recommended.")

if not recommendations:
    recommendations.append("✅ Maintain your current healthy lifestyle and continue regular preventive care.")

for item in recommendations:
    st.info(item)

# Visualization
st.markdown("## 📈 Risk Factor Visualization")

chart_data = pd.DataFrame({
    "Risk Factor": ["Age", "Smoking", "Family History", "Exercise", "Alcohol", "BMI", "Stress"],
    "Contribution": [
        2 if age > 50 else 0,
        3 if smoking == "Regular Smoker" else 1 if smoking == "Occasional Smoker" else 0,
        3 if family_history == "Yes" else 0,
        2 if exercise == "Low" else 0,
        2 if alcohol == "Frequently" else 0,
        2 if bmi >= 30 else 0,
        2 if stress == "High" else 0
    ]
})

fig = px.bar(
    chart_data,
    x="Risk Factor",
    y="Contribution",
    color="Contribution",
    text="Contribution",
    title="Cancer Risk Factor Contribution Analysis",
    color_continuous_scale="Teal"
)

st.plotly_chart(fig, width="stretch")
st.markdown("""
<div class="workflow-box">
<h3>⚙ Workflow Automation & AI Integration</h3>
<p>
The system automatically processes patient input data through AI-assisted rule-based logic,
calculates the risk score, generates personalized prevention recommendations,
and creates a downloadable patient risk report.
</p>
</div>
""", unsafe_allow_html=True)

# Workflow automation
st.markdown("""
<div class="workflow-box">
<h3>⚙ Workflow Automation & AI Integration</h3>
<p>
The system automatically processes patient input data through AI-assisted rule-based logic,
calculates the risk score, generates personalized prevention recommendations,
and creates a downloadable patient risk report.
</p>
</div>
""", unsafe_allow_html=True)

# Report
st.markdown("## 📄 Automated Patient Risk Report")

report = f"""
ONCOPREDICT AI - PATIENT RISK REPORT

Age: {age}
Weight: {weight} kg
Height: {height} cm
BMI: {bmi:.2f} ({bmi_status})

Smoking Habit: {smoking}
Family History: {family_history}
Exercise Level: {exercise}
Alcohol Consumption: {alcohol}
Stress Level: {stress}

Risk Score: {risk_score}/16
Risk Level: {risk_level}

AI-GENERATED RECOMMENDATIONS:
{chr(10).join(recommendations)}

Disclaimer:
This application is developed for educational and awareness purposes only and does not provide medical diagnosis.
"""

st.download_button(
    label="⬇ Download Automated Risk Report",
    data=report,
    file_name="OncoPredict_AI_Report.txt",
    mime="text/plain"
)

st.success("✅ AI workflow completed successfully.")
