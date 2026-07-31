# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant information, employment details, loan characteristics, and credit history.

The project combines a trained **XGBoost Classifier** with a **Flask REST API** backend and an interactive **Streamlit frontend**. Users can enter their financial, employment, loan, and credit information through the web interface and receive a predicted loan approval decision.

---

## 🚀 Live Application

### Try the Loan Approval Prediction System

👉 **https://loan-approvalsys-app.streamlit.app/**

The application provides an interactive interface where users can enter applicant and loan details and receive an instant prediction of:

- 🎉 **Loan Approved**
- ❌ **Loan Rejected**

> **Note:** The application backend is hosted on a free cloud service and may become idle after a period of inactivity. If the backend has been inactive, the first prediction request may take longer while the service wakes up. The application includes connection handling and retry logic to handle temporary backend availability issues.

---

## 📌 Project Overview

Loan approval decisions depend on multiple factors, including an applicant's income, employment experience, credit score, loan amount, loan purpose, and previous loan history.

This project demonstrates how Machine Learning can be used to build a classification system that predicts whether a loan application is likely to be approved or rejected.

The application follows a complete Machine Learning workflow:

1. Data collection and exploration
2. Data preprocessing
3. Feature engineering
4. Categorical feature encoding
5. Model training
6. Model evaluation
7. Model serialization
8. Flask REST API development
9. Streamlit frontend development
10. Cloud deployment

The system accepts applicant and loan-related information and uses a trained classification model to generate a predicted loan status.

---

## ✨ Features

- 🏦 Loan approval prediction
- 🤖 Machine Learning-based classification
- 📊 XGBoost Classifier
- 🌐 Interactive Streamlit web interface
- 🔌 Flask REST API for prediction
- 👤 Applicant information processing
- 💰 Income and employment analysis
- 💳 Credit score evaluation
- 🏠 Home ownership information
- 💵 Loan amount and interest rate analysis
- 📈 Loan-to-income ratio analysis
- 📚 Credit history analysis
- ⚠️ Previous loan default consideration
- 🔄 API request retry handling
- ⏳ Timeout handling for slow backend responses
- 🛡️ User-friendly error messages
- ☁️ Cloud deployment

---

## 🧠 Machine Learning Model

The application uses the **XGBoost Classifier** to predict loan approval status.

XGBoost is a powerful gradient boosting algorithm that builds an ensemble of decision trees sequentially. Each new tree attempts to improve the errors made by previous trees.

It is well suited for structured tabular datasets and classification problems involving a combination of numerical and categorical features.

The model was trained using applicant, employment, loan, and credit-related features.

---

## 📋 Input Features

The model uses the following features:

| Feature | Description |
|---|---|
| `person_age` | Applicant's age |
| `person_gender` | Applicant's gender |
| `person_education` | Applicant's education level |
| `person_income` | Applicant's annual income |
| `person_emp_exp` | Applicant's employment experience |
| `person_home_ownership` | Applicant's home ownership status |
| `loan_amnt` | Requested loan amount |
| `loan_intent` | Purpose or intent of the loan |
| `loan_int_rate` | Loan interest rate |
| `loan_percent_income` | Loan amount as a percentage of income |
| `cb_person_cred_hist_length` | Length of the applicant's credit history |
| `credit_score` | Applicant's credit score |
| `previous_loan_defaults_on_file` | Whether the applicant has previous loan defaults |

---

## 🎯 Target Variable

The model predicts the loan application status.

The prediction result is presented to the user as:

```text
Approved

or

Rejected
📊 Model Performance

The XGBoost Classifier achieved the following performance on the test dataset:

Metric	Rejected	Approved
Precision	95%	91%
Recall	98%	80%
F1-Score	96%	85%

Overall Accuracy: 94%

Performance Summary

The model achieved an overall accuracy of approximately 94%, indicating strong classification performance on the test dataset.

The model demonstrates particularly strong performance for the class representing rejected loan applications, with a recall of approximately 98%.

For approved loan applications, the model achieved:

91% Precision
80% Recall
85% F1-Score

These results indicate that the model performs well overall, while there is still potential to improve the identification of approved applications.

Model performance depends on the dataset, preprocessing techniques, train/test split, and model configuration. Results may vary when applied to new or unseen data.

🔄 Machine Learning Workflow

The overall workflow of the project is:

Loan Dataset
      │
      ▼
Data Exploration
      │
      ▼
Data Cleaning
      │
      ▼
Feature Selection
      │
      ▼
Categorical Feature Encoding
      │
      ▼
Train/Test Split
      │
      ▼
XGBoost Classifier
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Trained Model
      │
      ▼
Flask REST API
      │
      ▼
Streamlit Frontend
      │
      ▼
Loan Approval Prediction
🌐 Application Architecture

The application is divided into two major components.

1. Streamlit Frontend

The Streamlit application provides an interactive user interface.

Users enter:

Personal information
Education information
Employment information
Income information
Loan information
Credit information

The frontend then sends the entered information to the Flask REST API as a JSON request.

2. Flask REST API

The Flask backend acts as the Machine Learning prediction API.

The API:

Receives loan application data
Converts the JSON request into a DataFrame
Applies the required preprocessing
Aligns features with the trained model
Loads the trained XGBoost model
Generates a prediction
Returns the predicted loan status as JSON

The complete architecture can be represented as:

                   User
                     │
                     ▼
          Streamlit Web Interface
                     │
                     │ HTTP POST Request
                     ▼
              Flask REST API
                     │
                     ▼
          Data Preprocessing
                     │
                     ▼
         Feature Transformation
                     │
                     ▼
            XGBoost Classifier
                     │
                     ▼
         Loan Approval Prediction
                     │
                     ▼
          Flask JSON Response
                     │
                     ▼
         Streamlit Result Display
                     │
              ┌──────┴──────┐
              ▼             ▼
           APPROVED       REJECTED
🛠️ Technologies Used
Programming Language
Python
Data Processing
Pandas
NumPy
Machine Learning
Scikit-learn
XGBoost
Backend
Flask
Flask-CORS
Frontend
Streamlit
Model Persistence
Joblib
Deployment
Streamlit Community Cloud
Render
Version Control
Git
GitHub
📦 Installation
1. Clone the Repository

Clone the project repository:

git clone <repository-url>

Navigate to the project directory:

cd Loan_Approval_Prediction
2. Create a Virtual Environment

Create a Python virtual environment:

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate
3. Install Dependencies

Install the required packages:

pip install -r requirements.txt
▶️ Running the Application Locally

The application consists of a Flask backend and a Streamlit frontend.

Step 1: Start the Flask API

From the project root directory, run:

python app.py

The Flask API will run locally at:

http://127.0.0.1:5000

The prediction endpoint is:

POST /predict
Step 2: Start the Streamlit Frontend

Open a second terminal and run:

streamlit run streamlit_app/app.py

The Streamlit application will open in your browser.

The frontend communicates with the Flask backend to generate loan approval predictions.

🔌 API Request Example

The Flask API accepts loan application information in JSON format.

Example request:

{
    "person_age": 30,
    "person_gender": "male",
    "person_education": "Bachelor",
    "person_income": 75000,
    "person_emp_exp": 5,
    "person_home_ownership": "RENT",
    "loan_amnt": 10000,
    "loan_intent": "PERSONAL",
    "loan_int_rate": 10.5,
    "loan_percent_income": 0.13,
    "cb_person_cred_hist_length": 8,
    "credit_score": 720,
    "previous_loan_defaults_on_file": "No"
}

The API processes the request and returns a predicted loan status.

Example response:

{
    "predicted_loan_class": "Approved"
}

The actual prediction will depend on the input values and the trained Machine Learning model.

📁 Project Structure
Loan_Approval_Prediction/
│
├── dataset/
│   └── loan_approval_dataset.csv
│
├── models/
│   ├── loan_approval_model.joblib
│   └── train_columns.joblib
│
├── notebooks/
│   └── eda.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

The exact project structure may vary depending on the final repository organization.

💾 Model Serialization

The trained XGBoost model is saved using Joblib.

For example:

models/loan_approval_model.joblib

The training feature columns can also be saved separately:

models/train_columns.joblib

Saving the training columns allows the Flask API to ensure that incoming prediction data follows the same feature structure used during model training.

This helps prevent feature mismatch problems during inference.

☁️ Deployment

The application uses a two-part deployment architecture.

Streamlit Frontend

The interactive user interface is deployed using Streamlit Community Cloud.

Live application:

👉 https://loan-approvalsys-app.streamlit.app/

Flask Backend

The Flask Machine Learning API is deployed separately as a web service using a cloud hosting platform.

The Streamlit frontend sends prediction requests to the deployed Flask backend through the /predict endpoint.

This separation allows the frontend and backend to operate independently.

⚠️ Deployment Considerations

The Flask backend is hosted on a free cloud hosting service that may place the service into an idle state after a period of inactivity.

Therefore:

The first request after inactivity may take longer.
The backend may need time to wake up.
A prediction request may occasionally time out.
The application includes timeout and retry handling.
Users may need to wait a few moments or click Try Again if the backend is temporarily unavailable.

This is a limitation of the free hosting environment and does not necessarily indicate a problem with the Machine Learning model.

🔐 Responsible Use

This application is intended for educational and demonstration purposes.

The prediction generated by the Machine Learning model should not be considered a definitive financial decision or a substitute for professional financial or banking assessment.

Real-world loan approval decisions should consider additional factors, regulatory requirements, financial policies, fairness considerations, and human review.

🔮 Future Improvements

Possible future improvements include:

Improving model hyperparameter tuning
Addressing class imbalance
Improving recall for approved loan applications
Comparing XGBoost with other classification algorithms
Adding probability/confidence scores
Displaying prediction explanations
Adding SHAP-based model explainability
Adding visual credit and loan risk indicators
Implementing authentication for the API
Adding database support for prediction history
Adding automated model retraining
Implementing CI/CD pipelines
Improving frontend design and user experience
Adding monitoring and logging for the deployed API
🎯 Learning Outcomes

This project provided practical experience in:

Exploratory Data Analysis
Data preprocessing
Categorical feature encoding
Classification model development
XGBoost model training
Model evaluation
Precision, Recall, and F1-score analysis
Model serialization using Joblib
REST API development with Flask
Streamlit application development
Frontend-backend integration
JSON-based API communication
Error and timeout handling
Git and GitHub version control
Cloud deployment
Machine Learning application deployment
👨‍💻 Author

Rafaqat Muneer

Developed as an end-to-end Machine Learning project demonstrating the complete workflow from data preprocessing and model training to API development, interactive frontend development, and cloud deployment.

📄 License

This project is developed for educational, learning, and portfolio purposes.