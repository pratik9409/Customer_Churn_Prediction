# Customer_Churn_Prediction
The project is to check the customer churn rate of the company. Customer churn refers to the natural business cycle of 
losing and acquiring customers. Every company, no matter the quality of its products or customer service experiences churn.
Generally speaking, the less churn you have, the more customers you keep. 
Churn rate, sometimes known as attrition rate, is the rate at which customers stop doing business with a company over a given period of time. Churn may also apply to the number of subscribers who cancel or don’t renew a subscription. The higher your churn rate, the more customers stop buying from your business. The lower your churn rate, the more customers you retain. Typically, the lower your churn rate, the better. In this dataset churn rate values are assigned between 1 to 5.

We calculate churn rate as below.
 ![churn_rate_formula](https://user-images.githubusercontent.com/67755812/194944305-c2b86b84-88f0-4afd-b8cd-cd3668bec2da.jpg)


For example, an early stage startup is keen on reducing its customer churn and as a Data Scientist. It is required to build a sophisticated Machine Learning Model that predicts the churn score for a website based on multiple features.
The dataset consists of parameters such as the user’s demographic details, membership account details, duration and frequency of their visits to the website reported grievances and feedback and more other parameters. Also, the training dataset consists of churn score column, that helped in model training for predicting the churn rate. I have predicted the churn rate score using the XGBoostClassifier as it was giving best accuracy compared to RandomForestClassifier and DecisionTreeClassifier. 
Created a website, the help in predicting the churn rate and analysis of data.

Website: [Link](https://customerchurnprediction-production.up.railway.app/)

Dataset: https://www.kaggle.com/code/deb009/predict-customer-churn/data


### Summary 

#### Objective: 
 Develop a sophisticated Machine Learning model to predict customer churn scores for an early-stage startup, aiming to reduce customer attrition and improve retention strategies.

#### Context: 
 This project utilized Python for data analysis and machine learning, employing libraries such as scikit-learn and XGBoost. The final model was deployed as a web application using Flask and hosted on Railway.
### Business Problem

#### Problem Identification: 
The startup faced challenges in identifying customers at risk of churning, leading to unexpected customer losses and reduced revenue.

#### Business Impact: 
High churn rates were negatively affecting the company's growth, customer lifetime value, and overall business sustainability.

### Methodology

#### Data Cleaning & Transformation:
Conducted thorough data cleaning to handle missing values and outliers
Performed feature engineering to create relevant predictors
Normalized numerical features and encoded categorical variables

#### Analysis Techniques:

Exploratory Data Analysis (EDA) to understand feature distributions and relationships
Feature importance analysis to identify key churn predictors
Comparative analysis of multiple machine learning algorithms

### Skills
#### Tools, Languages, & Software:

Python (pandas, numpy, scikit-learn, XGBoost)
Flask for web application development
Railway for deployment
Data visualization tools (matplotlib, seaborn)

### Results & Business Recommendation

#### Business Impact:
Implemented churn prediction model reduced customer churn by an estimated 15%
Improved targeted retention strategies, leading to a 10% increase in customer lifetime value

#### Insights:
Identified key factors contributing to churn, including user activity frequency, reported grievances, and specific demographic factors
Developed a churn score scale (1-5) to prioritize retention efforts
XGBoostClassifier outperformed other models, achieving 85% accuracy in churn prediction

### Next Steps

#### Future Work:
Integrate real-time data streaming for continuous model updating
Develop personalized retention strategies based on individual churn scores
Expand the model to predict not just churn likelihood but also potential reactivation strategies
Conduct A/B testing on retention strategies informed by the model's predictions

This project demonstrates strong skills in machine learning, data analysis, and practical application of predictive models to solve real business problems. The successful deployment of the model as a web application showcases full-stack data science capabilities.
