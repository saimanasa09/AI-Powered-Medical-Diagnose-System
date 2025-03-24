import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_735641_16735286404943588.jpg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('D:\Medical_Diagnosis-main\AI-Powered-Medical-Diagnose-System\diabetes_model.sav', 'rb')),
    'parkinsons': pickle.load(open('D:\Medical_Diagnosis-main\AI-Powered-Medical-Diagnose-System\parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('D:\Medical_Diagnosis-main\AI-Powered-Medical-Diagnose-System\lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('D:\Medical_Diagnosis-main\AI-Powered-Medical-Diagnose-System\Thyroid_model.sav', 'rb'))
}


# ---- TOP NAVIGATION MENU ----
selected = option_menu(
    menu_title="AI Medical Diagnosis",
    options=["Diabetes Prediction", "Parkinsons Prediction", "Lung Cancer Prediction", "Hypo-Thyroid Prediction"],
    icons=["activity", "brain", "lungs", "thermometer"],
    menu_icon="stethoscope",
    default_index=0,
    orientation="horizontal"
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown("<h2>🩸 Diabetes Prediction</h2>", unsafe_allow_html=True)
    st.write("Enter the following details to predict diabetes:")
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
        Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
        BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
        SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    with col2:
        Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
        BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
        DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
        Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button("🔍 Predict Diabetes", use_container_width=True):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = "✅ The person **HAS Diabetes**" if diab_prediction[0] == 1 else "❌ The person **does NOT have Diabetes**"
        st.success(diab_diagnosis)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.markdown("<h2>🧠 Parkinson's Prediction</h2>", unsafe_allow_html=True)
    st.write("Enter the following details to predict Parkinson's disease:")
    col1, col2 = st.columns(2)
    with col1:
        fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
        fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
        flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
        Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
        Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
        RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
        PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
        DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
        Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
        Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
        APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    with col2:
        APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
        APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
        DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
        NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
        HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
        RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
        DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
        spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
        spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
        D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
        PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("🔍 Predict Parkinson's", use_container_width=True):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "✅ The person **HAS Parkinson's**" if parkinsons_prediction[0] == 1 else  "❌ The person **does NOT have Parkinson's**"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.markdown("<h2>🫁 Lung Cancer Prediction</h2>", unsafe_allow_html=True)
    st.write("Enter the following details to predict lung cancer:")
    col1, col2 = st.columns(2)
    with col1:
        GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
        AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
        SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
        YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
        ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
        PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
        CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
        FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    with col2:
        ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
        WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
        ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
        COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
        SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
        SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
        CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("🔍 Predict Lung Cancer", use_container_width=True):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "✅ The person **HAS Lung Cancer**" if lungs_prediction[0] == 1 else "❌ The person **does NOT have Lung Cancer**"
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.markdown("<h2>🦋 Hypo-Thyroid Prediction</h2>", unsafe_allow_html=True)
    st.write("Enter the following details to predict hypo-thyroid disease:")
    col1, col2 = st.columns(2)
    with col1:
        age = display_input('Age', 'Enter age of the person', 'age', 'number')
        sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
        on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
        tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    with col2:
        t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
        t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
        tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("🔍 Predict Hypo-Thyroid", use_container_width=True):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "✅ The person **HAS Hypo-Thyroid**" if thyroid_prediction[0] == 1 else "❌ The person **does NOT have Hypo-Thyroid**"
        st.success(thyroid_diagnosis)