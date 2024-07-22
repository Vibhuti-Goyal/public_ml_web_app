import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🩺")
# loading the saved models

diabetes_model = pickle.load(open('diabetes_saved_', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_saved', 'rb'))

liver_disease_model=pickle.load(open('Liver_disease_saved','rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                          'Liver Disease Prediction'],
                           menu_icon='👨🏻‍⚕️',
                          icons=['person','heart','activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
  
  
    #liver disease prediction page
    if(selected == 'Liver Disease Prediction'):
  
      st.title("Liver disease Prediction using ML")
      col1,col2,col3=st.columns(3)
  
      with col1:
        Age=st.text_input("Age")
      with col2:
        Gender=st.text_input("Gender: Male (0) or Female (1)")
      with col3:
         BMI=st.text_input("Body Mass Index")
  
      with col1:
        AlcoholConsumption=st.text_input("Alcohol consumption")
      with col2:
        Smoking=st.text_input("Smoking: No (0) or Yes (1) ")
      with col3:
        GeneticRisk=st.text_input("Genetic Risk: Low (0), Medium (1), High (2)")
      with col1:
        PhysicalActivity=st.text_input("Physical Activity")
      with col2:
        Diabetes=st.text_input("Diabetes: No (0) or Yes (1)")
      with col3:
        Hypertension=st.text_input("Hypertension: No (0) or Yes (1)")
      with col1:
        LiverFunctionTest=st.text_input("Liver Function Test")
  
      liver_dia = " "
      if st.button("Liver Disease Test Result"):
        liver_prediction=liver_disease_model.predict([[Age,Gender,BMI,AlcoholConsumption,Smoking,GeneticRisk,PhysicalActivity,Diabetes,Hypertension,LiverFunctionTest]])
        if(liver_prediction[0]==1):
          liver_dia="Person is having Liver disease"
        else:
          liver_dia="Person does not have any Liver disease"
    st.success(liver_dia)

    
    
        
    
    


    
        
    
