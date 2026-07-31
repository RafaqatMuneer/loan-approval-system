# Loan Approval Prediction System using XGBoost

## Overview

This project is an end-to-end Machine Learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant, financial, and credit-related information. The application includes model training, a Flask REST API for prediction, and a Streamlit-based user interface.

## Features

- Loan approval prediction using XGBoost Classifier
- Interactive Streamlit user interface
- Flask REST API for model inference
- Automatic data preprocessing using Scikit-learn Pipeline
- One-Hot Encoding for categorical features
- Model serialization using Joblib

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Streamlit
- Joblib

## Dataset Features

### Personal Information
- Person Age
- Person Gender
- Education Level

### Employment Information
- Annual Income
- Employment Experience
- Home Ownership

### Loan Information
- Loan Amount
- Loan Intent
- Interest Rate
- Loan Percent Income

### Credit Information
- Credit History Length
- Credit Score
- Previous Loan Defaults

## Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | **94%** |
| Precision | Rejected: **95%**, Approved: **91%** |
| Recall | Rejected: **98%**, Approved: **80%** |
| F1-Score | Rejected: **96%**, Approved: **85%** |

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd loan-approval
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the Flask API

```bash
python app.py
```

### 2. Launch the Streamlit Frontend

```bash
streamlit run streamlit_app/app.py
```

## Project Workflow

1. Data Collection and Exploration
2. Data Preprocessing
3. Feature Encoding using OneHotEncoder
4. Model Training using XGBoost Classifier
5. Model Evaluation
6. Save Trained Pipeline using Joblib
7. Flask API Development
8. Streamlit User Interface

## Project Structure

```text
loan-approval/
│
├── dataset/
├── models/
│   └── loan_approval_model.joblib
├── streamlit_app/
│   └── app.py
├── app.py
├── requirements.txt
└── README.md
```

## Prediction Output

The application predicts one of the following classes:

- ✅ Approved
- ❌ Rejected

## Author

Developed as an end-to-end Machine Learning capstone project using Python, Scikit-learn, XGBoost, Flask, and Streamlit.
