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