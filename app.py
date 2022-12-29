import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import base64

st.set_page_config(layout="wide")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Campus Placement Prediction</h1>", unsafe_allow_html=True)

# Load the data
data = pd.read_csv('train.csv')

st.markdown("<h4 style='text-align: center; color: white;'>Student Details</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Please enter student details for placement prediction</h5>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3, gap="large")

with col1:
    gender = st.selectbox("**Gender**", ("M","F"))
    if gender == 'M':
        st.write("Gender:",'**Male**')
    else:
        st.write("Gender:",'**Female**')
        
    ssc_p = st.number_input('**Secondary Education percentage- 10th Grade**', min_value=0, max_value=100)
    st.write('10th Grade Percentage:',ssc_p)
    
    ssc_b = st.selectbox("**Board of Education(10th grade)**", ('Central', 'Others'))
    if ssc_b == 'Central':
        st.write("Board in 10th grade:",'**Central**')
    else:
        st.write("Board in 10th grade:",'**Others**')
        
    hsc_p = st.number_input('**Higher Secondary Education percentage- 12th Grade**', min_value=0, max_value=100)
    st.write('12th Grade Percentage:',hsc_p)
    
    hsc_b = st.selectbox("**Board of Education(12th grade)**", ('Central', 'Others'))
    if hsc_b == 'Central':
        st.write("Board in 12th grade:",'**Central**')
    else:
        st.write("Board in 12th grade:",'**Others**')

with col2:    
    hsc_s = st.selectbox("**Specialization in Higher Secondary Education(12th Grade)**", ('Science', 'Commerce', 'Other'))
    if hsc_s == 'Science':
        st.write("Specialization in 12th Gorade:", '**Science**')
    elif hsc_s == 'Commerce':
        st.write("Specialization in 12th Gorade:", '**Commerce**')
    else :
        st.write("Specialization in 12th Gorade:", '**Arts**')
        
    degree_p = st.number_input('**Degree Percentage**', min_value=0, max_value=100)
    st.write('Degree Percentage:',degree_p)
  
    degree_t = st.selectbox("**Under Graduation(Degree type)- Field of Degree Education**", ('Sci&Tech', 'Comm&Mgmt', 'Others'))
    if degree_t == 'Sci&Tech':
        st.write("Degree Type:", '**Sci&Tech**')
    elif degree_t == 'Comm&Mgmt':
        st.write("Degree Type:", '**Comm&Mgmt**')
    else:
        st.write("Degree Type:", '**Others**')
        
    workex = st.selectbox("**Work Experience**", ('Yes', 'No'))
    if workex == 'Yes':
        st.write("Gender:",'**Male**')
    else:
        st.write("Gender:",'**Female**')
    
    etest_p = st.number_input('**Employability test percentage ( conducted by college)**', min_value=0, max_value=100)
    st.write('Employability test percentage:',etest_p)
    
with col3:       
    specialisation = st.selectbox("**Post Graduation(MBA)- Specialization**", ('Mkt&HR', 'Mkt&Fin'))
    if specialisation == 'Mkt&HR':
        st.write("MBA- Specialization:",'**Mkt&HR**')
    else:
        st.write("MBA- Specialization:",'**Mkt&Fin**')
        
    mba_p = st.number_input('**MBA percentage**', min_value=0, max_value=100)
    st.write('MBA percentage:',mba_p)
    
    status = st.selectbox("**Status of placement**", ('Placed', 'Not Placed'))
    if status == 'Placed':
        st.write("Status of placement:",'**Placed**')
    else:
        st.write("Status of placement:",'**Not Placed**')
    
    salary = st.number_input('**Salary offered by corporate to candidates**', min_value=0)
    st.write('Salary offered:',salary)
    
# Store the user input in a data frame
df = pd.DataFrame(
    np.array([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status, salary]]), 
    columns=['Gender', '10th%', 'ssc_b', '12th%', 'hsc_b', 'hsc_s', 'graduation%', 'degree_t', 'workex', 'Employee_test%', 'specialisation', 'mba_p', 'status', 'salary'])

st.caption("Your details are:")
st.table(df)

# Load the saved model
import pickle
model = open('model_pkl', 'rb')
pickle_model = pickle.load(model)

# Load the saved pipeline
pipe = open('pipeline.pkl', 'rb')
pipeline = pickle.load(pipe)

# Prediction
if st.button("Predict Placement"):
    # Transform the data
    data_transformed = pipeline.transform(df)
    prediction = pickle_model.predict(data_transformed)
    st.success('The student will {} get placed'.format(prediction))

st.markdown("<h5 style='text-align: center; color: white;'>About The Model</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>This model is built using Support Vector Classifier(SVC) algorithm</h6>", unsafe_allow_html=True)