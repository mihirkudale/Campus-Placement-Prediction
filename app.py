import streamlit as st
import pandas as pd
import numpy as np

# Title of the page
st.title("Campus Placement Prediction")

st.write("This application is a streamlit dashboard to **predict the placement of students**")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load the data
data = pd.read_csv('Placement_Data_Full_Class.csv')

st.markdown("##### Student Details")

st.caption("Please enter student details for placement prediction")

gender = st.selectbox("Gender", ('M', 'F'))
if gender == 'M':
    st.write("Gender:",'**Male**')
else:
    st.write("Gender:",'**Female**')
        
ssc_p = st.number_input('Secondary Education percentage- 10th Grade', min_value=0, max_value=100)
st.write('10th Grade Percentage:',ssc_p)
    
ssc_b = st.selectbox("Board of Education(10th grade)", ('Central', 'Others'))
if ssc_b == 'Central':
    st.write("Board in 10th grade:",'**Central**')
else:
    st.write("Board in 10th grade:",'**Others**')
    
hsc_p = st.number_input('Higher Secondary Education percentage- 12th Grade', min_value=0, max_value=100)
st.write('12th Grade Percentage:',hsc_p)
    
hsc_b = st.selectbox("Board of Education(12th grade)", ('Central', 'Others'))
if hsc_b == 'Central':
    st.write("Board in 12th grade:",'**Central**')
else:
    st.write("Board in 12th grade:",'**Others**')
        
hsc_s = st.selectbox("Specialization in Higher Secondary Education(12th Grade)", ('Science', 'Commerce', 'Other'))
if hsc_s == 'Science':
    st.write("Specialization in 12th Gorade:", '**Science**')
elif hsc_s == 'Commerce':
    st.write("Specialization in 12th Gorade:", '**Commerce**')
else :
    st.write("Specialization in 12th Gorade:", '**Arts**')
        
degree_p = st.number_input('Degree Percentage', min_value=0, max_value=100)
st.write('Degree Percentage:',degree_p)
        
degree_t = st.selectbox("Under Graduation(Degree type)- Field of Degree Education", ('Sci&Tech', 'Comm&Mgmt', 'Others'))
if degree_t == 'Sci&Tech':
    st.write("Degree Type:", '**Sci&Tech**')
elif degree_t == 'Comm&Mgmt':
    st.write("Degree Type:", '**Comm&Mgmt**')
else:
    st.write("Degree Type:", '**Others**')
            
workex = st.selectbox("Work Experience", ('Yes', 'No'))
if workex == 'Yes':
    st.write("Gender:",'**Male**')
else:
    st.write("Gender:",'**Female**')
            
etest_p = st.number_input('Employability test percentage ( conducted by college)', min_value=0, max_value=100)
st.write('Employability test percentage:',etest_p)
        
specialisation = st.selectbox(" Post Graduation(MBA)- Specialization", ('Mkt&HR', 'Mkt&Fin'))
if specialisation == 'Mkt&HR':
    st.write("MBA- Specialization:",'**Mkt&HR**')
else:
    st.write("MBA- Specialization:",'**Mkt&Fin**')
            
mba_p = st.number_input('MBA percentage', min_value=0, max_value=100)
st.write('MBA percentage:',mba_p)
        
status = st.selectbox("Status of placement", ('Placed', 'Not Placed'))
if status == 'Placed':
    st.write("Status of placement:",'**Placed**')
else:
    st.write("Status of placement:",'**Not Placed**')
            
salary = st.number_input('Salary offered by corporate to candidates', min_value=0)
st.write('Salary offered:',salary)

# Store the user input in a data frame
df = pd.DataFrame(
    np.array([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status, salary]]), 
    columns=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p', 'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p', 'status', 'salary'])

st.caption("Your details are:")
st.table(df)

# # Load the saved model
# import joblib
# model = joblib.load('model_joblib')

# Get the predictions
# prediction = model.predict(df)
st.subheader("Prediction")
# st.write("The student will be:",prediction)