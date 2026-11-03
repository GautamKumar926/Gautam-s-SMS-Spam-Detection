
import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩"
)

st.title("📩 SMS Spam Detection")
st.write("Machine Learning Based SMS Classification")

st.divider()

sms = st.text_area(
    "Enter Your SMS Message",
    placeholder="Type your message here..."
)

if st.button("Check SMS"):

    if sms.strip() == "":
        st.warning("Please enter an SMS message.")

    else:
        prediction = model.predict([sms])[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE DETECTED!")
            st.write("This SMS may be unwanted or fraudulent.")
        else:
            st.success("✅ HAM MESSAGE")
            st.write("This SMS is classified as genuine.")

st.divider()

st.subheader("Project Information")
st.write("Algorithm: Multinomial Naive Bayes")
st.write("Feature Extraction: TF-IDF")
st.write("Accuracy: 96.05%")

st.caption("IML Mini Project | SMS Spam Detection")
