# Customer-Churn-Prediction

## What is Customer Churn? Why is it necessary to detect it well in advance?

<p>Customer churn is defined as when customers or subscribers discontinue doing business with a firm or service. Customer churn, also known as customer attrition, is critical metric because retaining existing customers is much less exorbitant than acquiring new customers – earning business from new customers requires working leads all the way through the sales funnel, leveraging your marketing and sales resources throughout the process. Customer retention, on the other hand, is usually more cost-effective because you've already gained your consumers' confidence and loyalty.</p>

<p>Since customer attrition stifles growth, businesses should have a mechanism for estimating client churn over time. Organizations may assess their client retention success rates and identify strategies for improvement by being aware of and tracking churn rate. The overall number of customers lost, the percentage of customers lost compared to the company's entire customer count, the value of recurring business lost, or the percent of recurring value lost are all ways that different businesses assess customer churn rate. Other companies assess churn rate over a certain time period, such as quarters or fiscal years.</p>

<p>One of the most prominent methods for calculating customer churn is to divide the total number of customers a firm has at the start of a certain time period by the number of customers lost during that same time period.</p>


## Deployed Web Application

Link: https://customer-churn-prediction-sam.herokuapp.com/

![Customer Churn Prediction](https://miro.medium.com/max/1400/1*YhUxD22DhV3RYB8hXZ1ENg.png)
![Customer Churn](https://miro.medium.com/max/844/1*MyKDLRda6yHGR_8kgVvckg.png)
![Life Cycle of Customer Churn](https://miro.medium.com/max/456/1*Dvx1j18vyKyvLlIpxzVSmQ.png)

## Context

<p>Churn rate is a marketing metric that describes the number of customers who leave a business over a specific time period. Every user is assigned a prediction value that estimates their state of churn at any given time. This value is based on:</p>

<ul>
  <li>User demographic information</li>
  <li>Browsing behavior</li>
  <li>Historical purchase data among other information</li>
</ul>

<p>It factors in our unique and proprietary predictions of how long a user will remain a customer. This score is updated every day for all users who have a minimum of one conversion. The values assigned are between 1 and 5.</p>

## Content

<table>
  <tr>
    <th><b><em><strong>Feature</strong></em></b></th>
    <th><b><em><strong>Description</strong></em></b></th>
  </tr>
  <tr>
    <td>customer_id</td>
    <td>Represents the unique identification number of a customer.</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Represents the name of a customer.</td>
  </tr>
  <tr>
    <td>age</td>
    <td>Represents the age of a customer.</td>
  </tr>
  <tr>
    <td>security_no</td>
    <td>Represents a unique security number that is used to identify a person.</td>
  </tr>
  <tr>
    <td>region_category</td>
    <td>Represents the region that a customer belongs to.</td>
  </tr>
  <tr>
    <td>membership_category</td>
    <td>Represents the category of the membership that a customer is using.</td>
  </tr>
  <tr>
    <td>joining_date</td>
    <td>Represents the date when a customer became a member.</td>
  </tr>
  <tr>
    <td>joined_through_referral</td>
    <td>Represents whether a customer joined using any referral code or ID.</td>
  </tr>
  <tr>.
    <td>referral_id</td>
    <td>Represents a referral ID.</td>
  </tr>
  <tr>
    <td>preferred_offer_types</td>
    <td>Represents the type of offer that a customer prefers.</td>
  </tr>
  <tr>
    <td>medium_of_operation</td>
    <td>Represents the medium of operation that a customer uses for transactions.</td>
  </tr>
  <tr>
    <td>internet_option</td>
    <td>Represents the type of internet service that a customer uses.</td>
  </tr>
  <tr>
    <td>last_visit_time</td>
    <td>Represents the last time a customer visited the website.</td>
  </tr>
  <tr>
    <td>days_since_last_login</td>
    <td>Represents the no. of days since a customer last logged into the website.</td>
  </tr>
  <tr>
    <td>avg_time_spent</td>
    <td>Represents the average time spent by a customer on the website.</td>
  </tr>
  <tr>
    <td>avg_transaction_value</td>
    <td>Represents the average transaction value of a customer.</td>
  </tr>
  <tr>
    <td>avg_frequency_login_days</td>
    <td>Represents the no. of times a customer has logged in to the website.</td>
  </tr>
  <tr>
    <td>points_in_wallet</td>
    <td>Represents the points awarded to a customer on each transaction.</td>
  </tr>
  <tr>
    <td>used_special_discount</td>
    <td>Represents whether a customer uses special discounts offered.</td>
  </tr>
  <tr>
    <td>offer_application_preference</td>
    <td>Represents whether a customer prefers offers.</td>
  </tr>
  <tr>
    <td>past_complaint</td>
    <td>Represents whether a customer has raised any complaints earlier.</td>
  </tr>
  <tr>
    <td>complaint_status</td>
    <td>Represents whether the complaints(if any) raised by a customer were resolved or not.</td>
  </tr>
  <tr>
    <td>feedback</td>
    <td>Represents the feedback provided by a customer.</td>
  </tr>
  <tr>
    <td>churn_risk_score</td>
    <td>Represents the churn risk score that is either 0 or 1.</td>
  </tr>
</table>

