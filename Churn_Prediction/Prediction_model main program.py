import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the directory path for the input files
input_directory = "../input/"

# List all files under the input directory
file_list = []

for dirname, _, filenames in os.walk(input_directory):
    for filename in filenames:
        file_list.append(os.path.join(dirname, filename))
        print(os.path.join(dirname, filename))

# Read the "telecom_customer_churn.csv" file using pandas
file_path = "telecom_customer_churn.csv"
churn = pd.read_csv(file_path)
# Display the first few rows of the dataset
churn.head()




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv('telecom_customer_churn.csv')

# Remove the rows where 'Customer Status' is 'Joined'
data = data[data['Customer Status'] != 'Joined']

# Drop any columns that are not relevant for prediction
data = data.drop(['Customer ID', 'Churn Category', 'Churn Reason'], axis=1)

# Convert categorical variables into dummy/indicator variables
data = pd.get_dummies(data)

# Identify the target variable after conversion to dummy variables
target = 'Customer Status_Churned'

# Split the dataset into features (X) and target variable (y)
X = data.drop([target], axis=1)
Y = data[target]

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Use median of the columns for imputation
imputer = SimpleImputer(strategy='median')

# Fit on the training features and transform the features
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Initialize the Random Forest classifier
model = RandomForestClassifier()

# Train the model
model.fit(X_train, Y_train)

# Make predictions on the test set

Y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy)