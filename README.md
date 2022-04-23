# Welcome to Heart Diseases Predictor

## Walkthrough of the Repository  
This is a mini project for SC1015 Introduction to Data Science and Artificial Intelligence. This project aims to analyse all the factors affecting Heart Diseases and predict the probability of the user getting one.

1) The [Datasets Folder](Datasets/) contains the original BRFSS 2015 DATASET. Since its size is more than 500MB , it has been split into 3 zipfiles.
2) The [Presentation Folder](Presentation/) contains our PPT used to make our video.
3) The [Code Folder](Code/) contains the final ipynb file that includes cleaning the dataset, data exploration, and ML Model. The PKL file is the pickled ML Model extracted from the ipynb file. The py file is used to program streamlit and use the ML Model in PKL file to predict probability of heart disease. If you wish to run the streamlit webapp in your own device, you will have to edit lines 22 and 215 of heart_predict_final.py to update the address of heart.jpg and logReg_Model.pkl.


## Contributors 
1) Jai Jindal - Streamlit, Logistics Regression, Video Presentation , PPT , GITHUB
2) Livia Iriawan - Cleaning and Curating of Dataset , Video Presentation, PPT
3) Shayanthaviy Sivasankar- Logistic Regression , Video Presentation, PPT

## Problem Definition 

Identifying key health indicators that significantly affect heart diseases so that we can detect and prevent the factors having the greatest impact. 
1) What risk factors are most predictive of heart disease risk?
2) Can we use a subset of the risk factors to accurately build a webapp that can predict whether an individual has heart disease?


## Cleaning the Dataset 


## Machine Learning Model



## Application In Real Life

Using our ML Function through our Streamlit interface, users can:

1)Check for risk of heart diseases based on lifestyle practices
2)Look for recommendations to improve their overall health 
3)Understand the major factors affecting their health and consult their doctors before it is too late.


## Conclusion
Increase risk of Heart Diseases if:

1)High Cholesterol levels
2)High Blood Pressure 
3)Smoked more than 100 cigarettes in your life
4)Older age
5)Worsening Physical Health and Mental Health
6)No Physical Exercise

Factors such as number of fruits and vegetables eaten in a day, health insurance , and medical cost did not significantly affect the risk of heart diseases as compared to independent variables mentioned above . 


## What did we learn from this project?

Use of Streamlit for deploying webapp and incorporating a beautiful interface for our ML model pickled using joblib
Use of methods such as predict and predict_proba in logistic regression
Exploring Sklearn modules such as Pipeline , Standard scaler for scaling and further exploration of seaborn as a tool for visualization
Collaborating using GitHub
Cleaning and Curating datasets and binary and multiclass classification


## References
1) https://www.hindawi.com/journals/misy/2022/1410169/
2) https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system
3) https://slidesgo.com/theme/data-science-consulting
4) https://www.webmd.com/heart/heart-health-tips 
5) https://www.health.harvard.edu/healthbeat/10-small-steps-for-better-heart-health 
6) https://www.healthxchange.sg/heart-lungs/heart-disease/how-to-improve-heart-health-naturally
7) Buttar, H. S., Li, T., & Ravi, N. (2005). Prevention of cardiovascular diseases: Role of exercise, dietary interventions, obesity and smoking cessation. Experimental and clinical cardiology, 10(4), 229–249.
8) https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf
9) https://www.cdc.gov/pcd/issues/2019/19_0109.html
10) https://docs.streamlit.io/library/api-reference
7
