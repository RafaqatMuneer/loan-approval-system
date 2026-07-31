# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant, employment, loan, and credit information.

## 🚀 Live Demo

👉 https://loan-approvalsys-app.streamlit.app/

## ✨ Features

- Loan approval prediction using Machine Learning
- XGBoost Classifier
- Interactive Streamlit frontend
- Flask REST API backend
- JSON-based API communication
- Model serialization using Joblib
- Timeout and retry handling for API requests
- Cloud deployment

## 🧠 Machine Learning Model

**Algorithm:** XGBoost Classifier

The model uses the following features:

- Age
- Gender
- Education
- Annual Income
- Employment Experience
- Home Ownership
- Loan Amount
- Loan Intent
- Loan Interest Rate
- Loan Percent Income
- Credit History Length
- Credit Score
- Previous Loan Defaults

## 📊 Model Performance

| Metric | Rejected | Approved |
|---|---:|---:|
| Precision | 95% | 91% |
| Recall | 98% | 80% |
| F1-Score | 96% | 85% |

**Overall Accuracy: 94%**

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Streamlit
- Joblib
- Git & GitHub
- Render
- Streamlit Community Cloud

## 🔄 Workflow

```text
User Input
    ↓
Streamlit Frontend
    ↓
Flask REST API
    ↓
Data Preprocessing
    ↓
XGBoost Classifier
    ↓
Loan Prediction
    ↓
Approved / Rejected

```
## ▶️ Run Locally
Install dependencies:
```bash
pip install -r requirements.txt
```
Start the Flask API:
```bash
python app.py
```

Run the Streamlit application:
```bash
streamlit run streamlit_app/app.py
```

## 📁 Project Structure

Loan_Approval_Prediction/
│
├── dataset/
├── models/
├── notebooks/
├── streamlit_app/
│   └── app.py
├── app.py
├── requirements.txt
└── README.md

## ⚠️ Deployment Note

```text
The backend is hosted on a free cloud service and may become idle after inactivity. The first request after inactivity may take longer while the service wakes up. The application includes timeout and retry handling for temporary connection issues.


```

## 🔐 Disclaimer
```text
This project is developed for educational and demonstration purposes. Predictions should not be considered a definitive financial or banking decision.
```
## 👨‍💻 Author

```text
Rafaqat Muneer
```

```text
An end-to-end Machine Learning project demonstrating model training, evaluation, Flask API development, Streamlit frontend integration, and cloud deployment.
```





