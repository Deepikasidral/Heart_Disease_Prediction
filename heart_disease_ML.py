import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from streamlit_option_menu import option_menu
import time
import re
from chat_patterns import patterns
import os
import requests

BASE_URL = "http://127.0.0.1:8000"

# Load the saved heart disease prediction model
heart_model = pickle.load(open('saved_models/heart_model_save.sav', 'rb'))

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "user_email" not in st.session_state:
    st.session_state.user_email = None


# Function to generate a PDF of the result
def generate_pdf(result_message, title, ecg_graph=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, result_message)
    
    # Attach the ECG graph image if provided
    if ecg_graph:
        pdf.image(ecg_graph, x=10, y=100, w=190)

    return pdf.output(dest='S').encode('latin1')

# Sidebar for module selection
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                            ['User Profile',
                             'Heart Disease Prediction',
                             'Chatbot',
                             'ECG AI Analyzer',
                             'About Us'],
                            icons=['person', 'heart-pulse-fill', 'chat-left-heart', 'activity', 'info-circle-fill'],
                            default_index=0,
                            menu_icon='clipboard2-pulse-fill',
                            )

# Title and introductory message
st.title("Heart Disease Prediction System")
st.markdown("### Your Health is Our Priority!")

if selected == 'User Profile':
    st.subheader('User Profile')

    # ✅ IF USER IS LOGGED IN → SHOW PROFILE
    if st.session_state.user_id:

        st.success("Logged in successfully")

        st.write(f"**Email:** {st.session_state.user_email}")

        # 🔥 Logout Button
        if st.button("Logout"):
            st.session_state.user_id = None
            st.session_state.user_email = None
            st.rerun()

    # ❌ IF NOT LOGGED IN → SHOW FORMS
    else:
        option = st.selectbox("Choose Option", ["Register", "Login"])

        if option == "Register":
            email = st.text_input("Email")
            age = st.number_input("Age", min_value=0, max_value=120)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            password = st.text_input("Password", type="password")

            if st.button("Register"):
                res = requests.post(f"{BASE_URL}/users/register", json={
                    "Email": email,
                    "age": age,
                    "gender": gender,
                    "password": password
                })

                st.success(res.json().get("message"))

        elif option == "Login":
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                res = requests.post(f"{BASE_URL}/users/login", json={
                    "Email": email,
                    "age": 0,
                    "gender": "NA",
                    "password": password
                })

                if res.status_code == 200:
                    data = res.json()

                    if "user_id" in data:
                        st.session_state.user_id = data["user_id"]
                        st.session_state.user_email = email
                        st.success("Login Successful")
                        st.rerun()   # 🔥 refresh UI
                    else:
                        st.error("Login failed")

# 2. Heart Disease Prediction Section
if selected == 'Heart Disease Prediction':
    st.subheader('Heart Disease Prediction Using ML')

    # Input fields
    age = st.number_input('Age:', min_value=0, max_value=120)
    sex_mapping = {'Male': 1, 'Female': 0, 'Other': 2}
    selected_sex = st.selectbox('Gender:', list(sex_mapping.keys()))
    sex = sex_mapping[selected_sex]

    cp = st.selectbox('Chest Pain Type (0-3):', [0, 1, 2, 3])
    trestbps = st.number_input('Resting Blood Pressure (mmHg):', min_value=0)
    chol = st.number_input('Serum Cholesterol (mg/dl):', min_value=0)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl:', ['No', 'Yes'])
    restecg = st.selectbox('Resting ECG Result (0-2):', [0, 1, 2])
    thalach = st.number_input('Maximum Heart Rate Achieved:', min_value=0)
    exang = st.selectbox('Exercise Induced Angina:', ['No', 'Yes'])
    oldpeak = st.number_input('Oldpeak:', min_value=0.0, step=0.1)
    slope = st.selectbox('Slope (0-2):', [0, 1, 2])
    ca = st.selectbox('Number of Major Vessels (0-3):', [0, 1, 2, 3])
    thal = st.selectbox('Thalassemia (0-3):', [0, 1, 2, 3])

    # Prediction button
    if st.button('Test Result'):

        input_data = [[
            int(age), sex, int(cp), int(trestbps), int(chol),
            int(fbs == 'Yes'), int(restecg), int(thalach),
            int(exang == 'Yes'), float(oldpeak),
            int(slope), int(ca), int(thal)
        ]]

        pred = heart_model.predict(input_data)
        result = int(pred[0])

        # Result Message
        if result == 1:
            result_message = 'The person has heart disease.'
            st.error(result_message)
        else:
            result_message = 'The person does not have heart disease.'
            st.success(result_message)

        # ✅ Send to backend (MongoDB)
        if "user_id" in st.session_state:
            try:
                requests.post(f"{BASE_URL}/predictions/add_prediction", json={
                    "user_id": st.session_state.user_id,
                    "input_data": input_data[0],
                    "result": result
                })
            except:
                st.warning("Backend not connected")

        else:
            st.warning("Please login to save prediction")

        # ✅ PDF Download
        pdf_data = generate_pdf(result_message, title="Heart Disease Test Result")

        st.download_button(
            label="Download Result as PDF",
            data=pdf_data,
            file_name="heart_test_result.pdf",
            mime="application/pdf"
        )

        # ✅ Show History Button (Optional)
        if st.button("Show My History"):
            if "user_id" in st.session_state:
                res = requests.get(f"{BASE_URL}/predictions/get_predictions/{st.session_state.user_id}")
                data = res.json()

                for p in data["predictions"]:
                    st.write(p)
            else:
                st.warning("Please login first")

                
# 3. Fully Functional Chatbot Section
if selected == 'Chatbot':
    st.subheader('Welcome to Our Q&A Chatbot!')
    st.write('Feel free to ask any of the predefined questions below or type your own question:')

    # Input for user question
    user_question = st.text_input('Type your question here:', key='user_input')

    # Button to check if the question matches a predefined one
    if st.button('Get Answer'):
        if user_question.strip() == '':
            st.warning('Please enter a valid question.')
        else:
            response = "Sorry, I don't have an answer for that question."
            # Check each pattern against the user question
            for pattern, answer in patterns:
                if re.match(pattern, user_question.strip(), re.IGNORECASE):  # Match using regex
                    response = answer  # Get the specific answer
                    break

            st.write(f"**Chatbot:** {response}")

# 4. ECG AI Analyzer Section
if selected == 'ECG AI Analyzer':
    st.subheader('ECG AI Analysis')
    uploaded_ecg_file = st.file_uploader("Upload your ECG data CSV file", type="csv")

    if uploaded_ecg_file is not None:
        ecg_data = pd.read_csv(uploaded_ecg_file)
        st.write("Uploaded ECG Data:")
        st.write(ecg_data)

        # Assuming the CSV contains 'Time' and 'Voltage' columns for ECG plot
        if 'Time' in ecg_data.columns and 'Voltage' in ecg_data.columns:
            plt.figure(figsize=(10, 4))
            plt.plot(ecg_data['Time'], ecg_data['Voltage'])
            plt.title('ECG Heart Rate Over Time')
            plt.xlabel('Time (s)')
            plt.ylabel('Voltage (mV)')

            # Save the ECG graph as an image
            ecg_graph_path = "ecg_graph.png"
            plt.savefig(ecg_graph_path)
            plt.close()  # Close the plot to free up memory

            # Display the ECG graph in the Streamlit app
            st.pyplot(plt)

            # Offer to download the ECG report as a PDF with the ECG graph included
            if st.button("Download ECG Report"):
                pdf_data = generate_pdf("ECG Analysis Report", title="ECG Analysis Report", ecg_graph=ecg_graph_path)
                st.download_button(label="Download ECG Report as PDF", 
                                   data=pdf_data,
                                   file_name="ecg_report.pdf",
                                   mime="application/pdf")

# 5. About Us Section
if selected == 'About Us':
    st.subheader('About Us')
    st.write("""
    Welcome to the **Heart Disease Prediction System**, where cutting-edge technology meets compassionate care. 
    Our mission is to provide individuals with an accessible and intuitive platform to assess heart health through 
    advanced machine learning and AI techniques.

    We believe in empowering people with the tools to make informed decisions about their well-being. Our system 
    integrates heart disease predictions based on clinical symptoms, an AI-powered chatbot to answer any heart-related 
    queries, and an ECG analyzer to monitor real-time heart activity—ensuring a comprehensive approach to heart care.

    At the heart of this project is a team of dedicated healthcare professionals and data scientists who are passionate 
    about using technology to enhance healthcare. We are driven by a common goal—to reduce the impact of heart disease 
    worldwide by offering user-friendly, effective, and reliable tools for early detection and prevention.

    For any inquiries or feedback, feel free to reach out to us at **heartcare24@gmail.com**. Thank you for trusting 
    us with your heart health!
    """)
