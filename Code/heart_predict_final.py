# streamlit run "D:\jinda\python programs\A_DSAI_PROJECT\heart_predict_final.py"
# imports
import pandas as pd
import streamlit as st
import numpy as np
import joblib
import sklearn
import  PIL 


# Header
st.write("""
# Heart Disease Risk Prediction App 
""")

st.write(""" Welcome to our Heart Disease Risk Prediction App. Our aim is to use this platform to save lives by 
         alerting people of potential risks by analysing their lifestyle practices. We have collected/cleaned BRFSS 2015
         data which had inputs from over 400,000 people in the United States who were asked more than 330 questions. 
         We build a machine learning model to predict heart disease risk, and saved/exported the model for use in a Streamlit
         web app. Our model uses over 22 columns and more than 200,000 value rows after being cleaned.""")
  
image1=PIL.Image.open("D:\jinda\python programs\A_DSAI_PROJECT\heart.jpg")
st.image(image1,width=500)



st.write("### Answer the following 21 Questions: ")

# create the colums to hold user inputs
col1, col2, col3 = st.columns((3,3,3))

# gather user inputs

# 1. HighBP
highbp = col1.selectbox(
    "1. High Blood Pressure: Have you EVER been told by a doctor, nurse or other health professional that you have high Blood Pressure?",
    ('Yes', 'No'), index=0 )

# 2. HighChol
highchol = col2.selectbox(
    "2. High Cholesterol: Have you EVER been told by a doctor, nurse or other health professional that your Blood Cholesterol is high?",
    ('Yes', 'No'), index=1)

# 3. CholCheck
cholcheck = col3.selectbox(
    "3. About how long has it been since you last had your blood cholesterol checked? Put yes if less than 5 years, No if more than 5 years",
    ('Yes', 'No'), index=1)




# 4.BMI 
bmi = col1.number_input(
    '4. Enter your BMI : ', min_value=5, max_value=50, value=21)

# 5. Smoke
smoker = col2.selectbox(
    "5. Have you smoked atleast 100 cigarettes in your life?",
    ('Yes', 'No'), index=1)

# 6. Stroke
stroke = col3.selectbox(
    "6. Have you ever had stroke in your life?",
    ('No', 'Yes'), index=0)

#7. Diabetes
diabetes = col1.selectbox(
    "7. Have you ever had Diabetes in your life?",
    ('No Diabetes', 'Pre Diabetes', 'Diabetes'), index=0)

#8.PhysActivity
physActivity= col2.selectbox(
    "8. Are you physically active in your life?",
    ('No', 'Yes'), index=1)

#9.Fruits
fruits= col3.selectbox(
    "9. Do you have more than 1 fruit a day?",
    ('No', 'Yes'), index=1)

#10.Veggies
vegetables = col1.selectbox(
    "10. Do you have more than 1 vegetable a day?",
    ('No', 'Yes'), index=1)

#11.Alcohol consumption
Alcohol= col2.selectbox(
    "11. Are you a heavy drinker (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)?",
    ('No', 'Yes'), index=0)

#12.Alcohol consumption
healthplan= col3.selectbox(
    "12. Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare, or Indian Health Service?",
    ('No', 'Yes'), index=1)

#13.Alcohol consumption
medcost= col1.selectbox(
    "13. Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?",
    ('No', 'Yes'), index=1)

# 14. GenHlth
genhealth = col2.selectbox("14. General Health: How would you rank your General Health on a scale from 1 = Excellent to 5 = Poor? Consider physical and mental health.",
                         ('Excellent', 'Very Good', 'Good', 'Fair', 'Poor'), index=3)

#15.MentalHealth
menhlth = col3.number_input(
    '15. Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? : '
        , min_value=0, max_value=30, value=10)

#16.PhysicalHealth
Physhlth = col1.number_input(
    '16. Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? : '
        , min_value=0, max_value=30, value=10)

#17.Diff Walking
Diffwalk= col2.selectbox(
    "17. Did you have trouble walking in last 30 days?",
    ('No', 'Yes'), index=0)


#18.Sex
Sex= col3.selectbox(
    "18. Sex M/F:",
    ('Female', 'Male'), index=1)

# 19. Age
age = col1.selectbox(
    '19. Select your Age:', ('Age 18 to 24',
                            'Age 25 to 29',
                            'Age 30 to 34',
                            'Age 35 to 39',
                            'Age 40 to 44',
                            'Age 45 to 49',
                            'Age 50 to 54',
                            'Age 55 to 59',
                            'Age 60 to 64',
                            'Age 65 to 69',
                            'Age 70 to 74',
                            'Age 75 to 79',
                            'Age 80 or older'), index=4)

#20.education level
educa = col2.number_input(
    '20. What is your education level with 1 being to never attended school , 6 being graduated college? : '
        , min_value=0, max_value=6, value=4)

#21. Income
Income= col3.number_input(
    '21. What is your income level with 1 being less than 10,000$ to 8 being more than 75000$? : '
        , min_value=1, max_value=8, value=4)




# Create dataframe:
df1 = pd.DataFrame([[highbp,highchol,cholcheck,bmi,smoker,stroke,diabetes,physActivity,fruits,
                     vegetables,Alcohol,healthplan,
                     medcost,genhealth,menhlth,Physhlth,Diffwalk,Sex,age,educa,Income]], 
                    columns=["HighBP","HighChol","CholCheck","BMI","Smoker","Stroke","Diabetes","PhysActivity","Fruits","Veggies",
                             "HvyAlcoholConsump","AnyHealthcare","NoDocbcCost","GenHlth","MentHlt","PhysHlth","DiffWalk"
                             ,"Sex","Age","Education","Income"])




def prepare_df (df):
    
    # Age
    df['Age'] = df['Age'].replace({'Age 18 to 24': 1, 'Age 25 to 29': 2, 'Age 30 to 34': 3, 'Age 35 to 39': 4, 'Age 40 to 44': 5, 'Age 45 to 49': 6,
                               'Age 50 to 54': 7, 'Age 55 to 59': 8, 'Age 60 to 64': 9, 'Age 65 to 69': 10, 'Age 70 to 74': 11, 'Age 75 to 79': 12, 'Age 80 or older': 13})

    # HighChol
    df['HighChol'] = df['HighChol'].replace({'Yes': 1, 'No': 0})
    
    # HighBP
    df['HighBP'] = df['HighBP'].replace({'Yes': 1, 'No': 0})
    
    # GenHlth
    df['GenHlth'] = df['GenHlth'].replace(
    {'Excellent': 1, 'Very Good': 2, 'Good': 3, 'Fair': 4, 'Poor': 5})
    
    df['CholCheck'] = df['CholCheck'].replace({'Yes': 1, 'No': 0})
        
    df['Smoker'] = df['Smoker'].replace({'Yes': 1, 'No': 0})
    
    df['Stroke'] = df['Stroke'].replace({'Yes': 1, 'No': 0})

    df['Diabetes'] = df['Diabetes'].replace({'Diabetes':2,'Pre Diabetes': 1, 'No Diabetes': 0})
    
    df['Fruits'] = df['Fruits'].replace({'Yes': 1, 'No': 0})

    df['HvyAlcoholConsump'] = df['HvyAlcoholConsump'].replace({'Yes': 1, 'No': 0})

    df['PhysActivity'] = df['PhysActivity'].replace({'Yes': 1, 'No': 0})

    df['Veggies'] = df['Veggies'].replace({'Yes': 1, 'No': 0})

    df['AnyHealthcare'] = df['AnyHealthcare'].replace({'Yes': 1, 'No': 0})

    df['NoDocbcCost'] = df['NoDocbcCost'].replace({'Yes': 1, 'No': 0})

    df['DiffWalk'] = df['DiffWalk'].replace({'Yes': 1, 'No': 0})

    df['Sex'] = df['Sex'].replace({'Male': 1, 'Female': 0})   
    

    return df



df=prepare_df(df1)



log_reg_model = joblib.load('D:\jinda\python programs\A_DSAI_PROJECT\logReg_model.pkl')

if st.button('Click here to predict Heart Disease Risk'):

    # make the predictions
    prediction = log_reg_model.predict(df)
    prediction_probability = log_reg_model.predict_proba(df)


    if prediction == 0:
        st.markdown(f"**The probability that you'll have"
                f" heart disease is {round(prediction_probability[0][1] * 100, 2)}%."
                f" You are healthy!**")
   
    else:
        st.markdown(f"**The probability that you will have"
                f" heart disease is {round(prediction_probability[0][1] * 100, 2)}%."
                f" It sounds like you are not healthy. "
                f" You should refer to these sites to work towards improving your health"
                f" https://www.webmd.com/heart/heart-health-tips "
                f" https://www.health.harvard.edu/healthbeat/10-small-steps-for-better-heart-health "
                f" https://www.healthxchange.sg/heart-lungs/heart-disease/how-to-improve-heart-health-naturally**")
        




