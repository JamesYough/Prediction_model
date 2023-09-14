# Prediction_model
# Telecom Customer Churn Analysis

This repository contains code for analyzing telecom customer churn using machine learning techniques. The code is written in Python and utilizes popular libraries such as NumPy, pandas, matplotlib, seaborn, and scikit-learn.

## Dataset

The dataset used for this analysis is "telecom_customer_churn.csv". It contains information about telecom customers and their churn status. The dataset is preprocessed to remove irrelevant columns and convert categorical variables into dummy variables.

## Code Overview

The code performs the following steps:

1. Set the directory path for the input files.
2. List all files under the input directory.
3. Read the "telecom_customer_churn.csv" file using pandas.
4. Display the first few rows of the dataset.
5. Visualize the frequency of customer status using a countplot.
6. Split the dataset into training and testing sets.
7. Use the SimpleImputer class to handle missing values.
8. Initialize a Random Forest classifier.
9. Train the model using the training set.
10. Make predictions on the test set.
11. Evaluate the model's accuracy.
12. View the training set.

## Usage

To run the code, follow these steps:

1. Clone the repository.
2. Ensure that the required libraries are installed.
3. Place the "telecom_customer_churn.csv" file in the appropriate directory.
4. Execute the code.

## Results

The code outputs the accuracy of the trained model on the test set. Additionally, it displays the training set, which includes the imputed features and the target variable.

Feel free to explore and modify the code as needed for your own analysis.

Please note that this is a general template, and you may need to customize it further based on your specific requirements.

Let me know if there's anything else I can assist you with!
