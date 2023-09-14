import pandas as pd
import matplotlib.pyplot as plt
 # Load the dataset
data = pd.read_csv("telecom_customer_churn.csv")
 # Count the number of churned and non-churned customers
churn_counts = data["Customer Status"].value_counts()
 # Create a bar plot
plt.bar(churn_counts.index, churn_counts.values)
plt.xlabel("Churn Status")
plt.ylabel("Count")
plt.title("Distribution of Customer Churn")
plt.show()


churn_by_gender = churn.groupby('Gender')['Customer Status'].apply(lambda x: (x == 'Churned').mean()*100)
churn_by_age = churn.groupby('Age')['Customer Status'].apply(lambda x: (x == 'Churned').mean() * 100)
churn_by_marriage = churn.groupby('Married')['Customer Status'].apply(lambda x: (x == 'Churned').mean()*100)


# Visualize the churn_by_gender
plt.bar(churn_by_gender.index, churn_by_gender, color=["pink", "blue"])
plt.xlabel('Gender')
plt.ylabel('Churn Rate')
plt.title('CHURN RATE BY GENDER')
plt.show()

# Visualize the churn_by_age
plt.plot(churn_by_age.index, churn_by_age, color="red")
plt.xlabel('Age')
plt.ylabel('Churn Rate')
plt.title('CHURN RATE BY AGE')
plt.show()

#Visualize the churn rate according to marriage status
plt.bar(churn_by_marriage.index, churn_by_marriage, color=["red", "green"])
plt.xlabel('Marriage Status')
plt.ylabel('Churn Rate')
plt.title('CHURN RATE BY MARRIAGE')
plt.show()