#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib
from datetime import date


# In[2]:


year = date.today().year


# In[3]:


model = joblib.load('model.pkl')
model


# In[4]:


scaler = joblib.load('scaler.bin')
scaler


# In[5]:


membership_categories = ['Platinum Membership','Premium Membership','No Membership',
 'Gold Membership','Silver Membership','Basic Membership']
membership_val = [3,4,2,1,5,0]
membership_encoded = dict(zip(membership_categories,membership_val))
membership_encoded


# In[6]:


mediums_of_operation = ['?','Desktop','Smartphone','Both']
moo_val = [3,1,2,0]
medium_operation_encoded = dict(zip(mediums_of_operation,moo_val))
medium_operation_encoded


# In[7]:


joining_months = ['January','February','March','April','May','June','July','August','September','October','November','December']
months_encoded = [1,2,3,4,5,6,7,8,9,10,11,12]
joining_months_encoded = dict(zip(joining_months,months_encoded))
joining_months_encoded


# In[8]:


days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
days_encoded = [0,1,2,3,4,5,6]
days_of_week_encoded = dict(zip(days_of_week,days_encoded))
days_of_week_encoded


# In[9]:


app = Flask(__name__)


# In[10]:


@app.route("/")
def home():
    return render_template('home.html',current_year=year,weekdays=days_of_week,months=joining_months,operation_mediums=mediums_of_operation,mem_categories=membership_categories)


# In[11]:


@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        age = request.form['age'] #Range: (10,64)
        gender_selected = request.form['gender']
        gender = -5
        if gender_selected == 'Male':
            gender = 1
        elif gender_selected == 'Female': 
            gender = 0
        elif gender_selected == 'Unknown':
            gender = -1
        region_selected = request.form['region']
        region = -1
        if region_selected == 'Village': 
            region = 2
        elif region_selected == 'City': 
            region = 0
        elif region_selected == 'Town':
            region = 1
        membership_selected = request.form['membership_category']
        membership = membership_encoded[membership_selected]
        referral_selected = request.form['joined_through_referral']
        referral = -2
        if referral_selected == 'No':
            referral = 0
        elif referral_selected == 'Yes':
            referral = 1
        elif referral_selected == 'Unknown':
            referral = -1
        offer_selected = request.form['preferred_offer_types']
        preferred_offer_type = -1
        if offer_selected == 'Gift Vouchers/Coupons': 
            preferred_offer_type = 1
        elif offer_selected == 'Credit/Debit Card Offers': 
            preferred_offer_type = 0
        elif offer_selected == 'Without Offers':
            preferred_offer_type = 2
        mo_op_selected = request.form['medium_of_operation']
        medium = medium_operation_encoded[mo_op_selected]
        net_selected = request.form['internet_option']
        internet_option = -1
        if net_selected == 'Wi-Fi': 
            internet_option = 0
        elif net_selected == 'Mobile Data': 
            internet_option = 1
        elif net_selected == 'Fiber Optic':
            internet_option = 2
        days_since_last_login = request.form['days_since_last_login'] #Range: (0,30)
        avg_time_spent = request.form['avg_time_spent'] #Range: (0,801)
        avg_transaction_val = request.form['avg_transaction_val'] #Range: (800.460,80871.465)
        avg_frequency_login_days = request.form['avg_frequency_login_days'] #Range: (0,73)
        points_in_wallet = request.form['points_in_wallet'] #Range: (425.37,955.98)
        used_special_discount = request.form['used_special_discount']
        discount = -1
        if used_special_discount == 'No':
            discount = 0
        elif used_special_discount == 'Yes':
            discount = 1
        offer_application_preference = request.form['offer_application_preference']
        offer_app_pref = -1
        if offer_application_preference == 'No':
            offer_app_pref = 0
        elif offer_application_preference == 'Yes':
            offer_app_pref = 1
        past_complaint = request.form['past_complaint']
        complaint = -1
        if past_complaint == 'No':
            complaint = 0
        elif past_complaint == 'Yes':
            complaint = 1
        complaint_status_selected = request.form['complaint_status']
        complaint_status = -5
        if complaint_status_selected == 'Solved':
            complaint_status = 1
        elif complaint_status_selected == 'Unsolved':
            complaint_status = 0
        elif complaint_status_selected == 'Unknown':
            complaint_status = -1
        feedback_selected = request.form['feedback']
        feedback = -5
        if feedback_selected in ['Poor Product Quality','Too many ads','Poor Website','Poor Customer Service']:
            feedback = -1
        elif feedback_selected in ['Reasonable Price','User Friendly Website','Products always in Stock','Quality Customer Care']:
            feedback = 1
        elif feedback_selected in ['None']:
            feedback = 0
        joining_day = request.form['joining_day'] #Range: (1,31) 
        joining_year_selected = request.form['joining_year'] 
        joining_year = -1 
        if joining_year_selected == '2015':
            joining_year = 2015
        elif joining_year_selected == '2016':
            joining_year = 2016
        elif joining_year_selected == '2017':
            joining_year = 2017
        joining_month_selected = request.form['joining_month'] #Range: (1,12)
        joining_month = joining_months_encoded[joining_month_selected]
        joining_day_of_week_selected = request.form['joining_day_of_week'] #Range: (0,6)
        joining_day_of_week = days_of_week_encoded[joining_day_of_week_selected]
        last_visit_hour = request.form['last_visit_hour'] #Range: (0,23)
        last_visit_min = request.form['last_visit_min'] #Range: (0,59)
        last_visit_sec = request.form['last_visit_sec'] #Range: (0,59)
        
        X_test = scaler.transform([[
            age,
            gender,
            region,
            membership,
            referral,
            preferred_offer_type,
            medium,
            internet_option,
            days_since_last_login,
            avg_time_spent,
            avg_transaction_val,
            avg_frequency_login_days,
            points_in_wallet,
            discount,
            offer_app_pref,
            complaint,
            complaint_status,
            feedback,
            joining_day,
            joining_year,
            joining_month,
            joining_day_of_week,
            last_visit_hour,
            last_visit_min,
            last_visit_sec
        ]])
        
        predictions = model.predict(X_test)
        output = predictions[0]
        
        if output == 0:
            return render_template('home.html',current_year=year,weekdays=days_of_week,months=joining_months,operation_mediums=mediums_of_operation,mem_categories=membership_categories,prediction_text="The customer with the given details is very likely to stop acquiring the services of the respected company.")
        elif output == 1:
            return render_template('home.html',current_year=year,weekdays=days_of_week,months=joining_months,operation_mediums=mediums_of_operation,mem_categories=membership_categories,prediction_text="The customer with the given details is highly likely to continue getting the services of the respected company.")


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

