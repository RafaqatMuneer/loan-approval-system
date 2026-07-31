from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from xgboost import XGBClassifier

# intiating Flask app
app = Flask(__name__)

with open("models/loan_approval_model.joblib", "rb") as f:
    model = joblib.load(f)

# creating home
@app.route("/")
def home():
    return {"message": "Salary Prediction API"}

# creating prediction endpoint of the API
@app.route("/predict", methods = ["POST"])

def predict():
    # getting json data from front end or postman for testing

    data = request.json
    #Input as pandas dataframe for using get_dummies

    input_df = pd.DataFrame([{
            "person_age": int(data["person_age"]),
            "person_gender": str(data["person_gender"]),
            "person_education": str(data["person_education"]),
            "person_income": float(data["person_income"]),
            "person_emp_exp": int(data["person_emp_exp"]),
            "person_home_ownership": str(data["person_home_ownership"]),
            "loan_amnt": float(data["loan_amnt"]),
            "loan_intent": str(data["loan_intent"]),
            "loan_int_rate": float(data["loan_int_rate"]),
            "loan_percent_income": float(data["loan_percent_income"]),
            "cb_person_cred_hist_length": float(data["cb_person_cred_hist_length"]),
            "credit_score": int(data["credit_score"]),
            "previous_loan_defaults_on_file": str(data["previous_loan_defaults_on_file"])
        }])

    prediction = model.predict(input_df)

    result = "Approved" if prediction[0] == 1 else "Rejected"

    return jsonify({
        "predicted_loan_class": result
    })

if __name__ == "__main__":
    app.run(debug=True)
