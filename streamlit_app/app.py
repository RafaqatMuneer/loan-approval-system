import streamlit as st
import requests
import time

st.set_page_config(page_title="Loan Approval Prediction System", page_icon="🏦", layout="centered")

st.title("🏦 Loan Approval Prediction System")
st.write("Enter the applicant details below to predict the loan approval status.")

st.subheader("👤 Personal Information")
c1,c2=st.columns(2)
with c1:
    person_age=st.slider("Age",20,100,30)
    person_gender=st.selectbox("Gender",["female","male"])
with c2:
    person_education=st.selectbox("Education",["High School","Associate","Bachelor","Master","Doctorate"])
    person_emp_exp=st.slider("Employment Experience (Years)",0,60,5)

st.subheader("💼 Employment Information")
c1,c2=st.columns(2)
with c1:
    person_income=st.number_input("Annual Income (USD)",8000.0,7200766.0,70000.0,1000.0)
    person_home_ownership=st.selectbox("Home Ownership",["OWN","MORTGAGE","OTHER","RENT"])
with c2:
    loan_amnt=st.number_input("Loan Amount (USD)",500.0,35000.0,8000.0,500.0)
    loan_intent=st.selectbox("Loan Purpose",["EDUCATION","MEDICAL","VENTURE","HOMEIMPROVEMENT","PERSONAL","DEBTCONSOLIDATION"])

st.subheader("🏦 Credit Information")
c1,c2=st.columns(2)
with c1:
    loan_int_rate=st.slider("Interest Rate (%)",5.42,20.0,11.0,0.01)
    loan_percent_income=st.slider("Loan Percent Income",0.0,0.66,0.14,0.01)
    previous_loan_defaults_on_file=st.selectbox("Previous Loan Default",["No","Yes"])
with c2:
    cb_person_cred_hist_length=st.slider("Credit History Length (Years)",2.0,30.0,6.0,1.0)
    credit_score=st.slider("Credit Score",390,850,640)

b1,b2=st.columns(2)
with b1:
    predict=st.button("✅ Predict",use_container_width=True)
with b2:
    if st.button("🔄 Reset",use_container_width=True):
        st.rerun()

# Loan Prediction
# ==========================
if predict:

    payload = {
        "person_age": person_age,
        "person_gender": person_gender,
        "person_education": person_education,
        "person_income": person_income,
        "person_emp_exp": person_emp_exp,
        "person_home_ownership": person_home_ownership,
        "loan_amnt": loan_amnt,
        "loan_intent": loan_intent,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": previous_loan_defaults_on_file
    }

    # Flask API URL
    API_URL = "http://127.0.0.1:5000/predict"

    # Number of attempts
    max_retries = 3

    # Store prediction result
    result = None

    try:

        # Try the API request multiple times
        for attempt in range(max_retries):

            try:

                # Display loading message
                if attempt == 0:
                    message = (
                        "🔄 Connecting to the loan prediction service..."
                    )
                else:
                    message = (
                        f"🔄 Retrying prediction "
                        f"({attempt + 1}/{max_retries})..."
                    )

                # Show spinner while waiting for API response
                with st.spinner(message):

                    response = requests.post(
                        API_URL,
                        json=payload,
                        timeout=60
                    )

                # Successful prediction
                if response.status_code == 200:

                    result = response.json()
                    break

                # Server error
                elif response.status_code >= 500:

                    if attempt < max_retries - 1:
                        time.sleep(5)
                        continue

                    else:
                        st.warning(
                            "⚠️ The loan prediction service is "
                            "temporarily unavailable. "
                            "Please try again in a moment."
                        )

                # Other HTTP errors
                else:

                    st.warning(
                        "⚠️ Unable to process the loan prediction. "
                        "Please check your inputs and try again."
                    )
                    break

            # Request timeout
            except requests.exceptions.Timeout:

                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue

                else:
                    st.warning(
                        "⏳ The prediction service is taking "
                        "longer than expected. "
                        "Please try again in a moment."
                    )

            # Connection error
            except requests.exceptions.ConnectionError:

                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue

                else:
                    st.warning(
                        "🔌 The loan prediction service is "
                        "currently unavailable. "
                        "Please wait a few seconds and try again."
                    )

            # Other request errors
            except requests.exceptions.RequestException:

                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue

                else:
                    st.warning(
                        "⚠️ We couldn't connect to the prediction "
                        "service. Please try again shortly."
                    )

        # Display prediction result
        if result:

            predicted_class = result["predicted_loan_class"]

            if predicted_class == "Approved":

                st.success(
                    "🎉 Loan Status: APPROVED"
                )

            else:

                st.error(
                    "❌ Loan Status: REJECTED"
                )

        # Try Again button
        elif result is None:

            if st.button(
                "🔄 Try Again",
                key="retry_loan_prediction"
            ):
                st.rerun()

    # Final safety net
    except Exception:

        st.warning(
            "⚠️ Something went wrong while processing "
            "your loan prediction. "
            "Please try again in a few moments."
        )

# if predict:
#     payload={
#         "person_age":person_age,
#         "person_gender":person_gender,
#         "person_education":person_education,
#         "person_income":person_income,
#         "person_emp_exp":person_emp_exp,
#         "person_home_ownership":person_home_ownership,
#         "loan_amnt":loan_amnt,
#         "loan_intent":loan_intent,
#         "loan_int_rate":loan_int_rate,
#         "loan_percent_income":loan_percent_income,
#         "cb_person_cred_hist_length":cb_person_cred_hist_length,
#         "credit_score":credit_score,
#         "previous_loan_defaults_on_file":previous_loan_defaults_on_file
#     }
#     try:
#         r=requests.post("http://127.0.0.1:5000/predict",json=payload)
#         if r.status_code==200:
#             result=r.json()["predicted_loan_class"]
#             if result=="Approved":
#                 st.success("🎉 Loan Status: APPROVED")
#             else:
#                 st.error("❌ Loan Status: REJECTED")
#         else:
#             st.error(r.text)
#     except Exception as e:
#         st.error(f"Connection Error: {e}")

with st.expander("ℹ About the Model"):
    st.markdown("""
**Algorithm:** XGBoost Classifier

### Performance
- Accuracy: **94%**
- Precision: Rejected **95%**, Approved **91%**
- Recall: Rejected **98%**, Approved **80%**
- F1-Score: Rejected **96%**, Approved **85%**

This application predicts whether a loan application is likely to be approved based on applicant, employment, loan and credit information.
""")
