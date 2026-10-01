# 🍔 Food Delivery Time Prediction Using Snowflake ML

An end-to-end machine learning project that predicts food delivery time using a Random Forest Regressor, with data preparation, model training, evaluation, model registration, and warehouse inference performed using Snowflake and Snowflake ML.

The project also includes an interactive Streamlit application that allows users to enter delivery details and receive an estimated delivery time.

---

## 📌 Project Overview

Food delivery platforms need to estimate how long an order will take to reach the customer.

Accurate delivery-time prediction can help with:

- Customer experience
- Delivery planning
- Driver allocation
- Operational efficiency
- Estimated arrival-time communication

This project builds a machine learning regression model to predict:

> **`Time_taken(min)` — the estimated time required to complete a food delivery.**

The project uses a Kaggle food-delivery dataset and implements an end-to-end workflow inside Snowflake.

---

# 🎯 Problem Statement

Given information about:

- Delivery person
- Restaurant location
- Customer location
- Distance
- Order time
- Pickup delay
- Weather
- Traffic
- Vehicle condition
- Order type
- Vehicle type
- Multiple deliveries
- Festival conditions
- City

predict the expected delivery time in minutes.

### Machine Learning Problem

**Regression**

### Target Variable
TIME_TAKEN

The original dataset represents this target as:

Time_taken(min)

🛠️ Technology Stack

Technology	Purpose
Snowflake	Data warehouse and ML infrastructure
Snowpark	Python access to Snowflake data
Snowflake ML	Model registration and inference
Python	Data preprocessing and model training
scikit-learn	Machine learning
Random Forest Regressor	Regression model
Streamlit	Interactive prediction application
SQL	Data preparation and warehouse inference
Kaggle	Dataset source
GitHub	Source-code and project documentation

📊 Dataset

The project uses a food-delivery dataset obtained from Kaggle.

The dataset contains approximately:

45,593 records
20 original columns

The target variable is:

Time_taken(min)

The raw dataset includes information such as:

ID
Delivery_person_ID
Delivery_person_Age
Delivery_person_Ratings
Restaurant_latitude
Restaurant_longitude
Delivery_location_latitude
Delivery_location_longitude
Order_Date
Time_Orderd
Time_Order_picked
Weatherconditions
Road_traffic_density
Vehicle_condition
Type_of_order
Type_of_vehicle
multiple_deliveries
Festival
City
Time_taken(min)

Dataset source: Kaggle
Add the exact Kaggle dataset URL here before publishing the repository.

Dataset URL:
https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset

🧪 Train/Test Split

The dataset was divided into training and testing datasets.

Training records: 36,394
Testing records: 9,199

The model was trained only on the training dataset.

The test dataset was kept separate for evaluating model performance.

🧩 Model Features

The model uses 17 input features.

Numerical Features
DELIVERY_PERSON_AGE
DELIVERY_PERSON_RATINGS
RESTAURANT_LATITUDE
RESTAURANT_LONGITUDE
DELIVERY_LOCATION_LATITUDE
DELIVERY_LOCATION_LONGITUDE
DISTANCE_KM
ORDER_HOUR
PICKUP_DELAY_MIN
VEHICLE_CONDITION
MULTIPLE_DELIVERIES
Categorical Features
WEATHERCONDITIONS
ROAD_TRAFFIC_DENSITY
TYPE_OF_ORDER
TYPE_OF_VEHICLE
FESTIVAL
CITY

🤖 Machine Learning Model

The project uses:

Random Forest Regressor

The model was implemented using scikit-learn.

Configuration:

RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

Categorical features were encoded using:

OneHotEncoder(handle_unknown="ignore")

A scikit-learn Pipeline was used to combine preprocessing and the Random Forest model.

Conceptually:

Input Data
    │
    ▼
ColumnTransformer
    │
    ├── Numerical Features
    │
    └── Categorical Features
             │
             ▼
       One-Hot Encoding
             │
             ▼
    Random Forest Regressor
             │
             ▼
      Delivery Time
      
📈 Model Performance

The trained Random Forest model was evaluated on the 9,199-row test dataset.

Metric	Result
MAE	3.20 minutes
RMSE	4.05 minutes
R² Score	0.8160
Training Rows	36,394
Test Rows	9,199
Mean Absolute Error
MAE = 3.20 minutes

On average, the absolute difference between the predicted delivery time and actual delivery time was approximately 3.20 minutes on the test set.

Root Mean Squared Error
RMSE = 4.05 minutes

RMSE gives greater weight to larger prediction errors.

R² Score
R² = 0.8160

The test-set R² indicates that the model explains a substantial portion of the variation in delivery time for this dataset.

These metrics are specific to this dataset and test split and should not be interpreted as a guarantee of performance on future or different delivery data.
