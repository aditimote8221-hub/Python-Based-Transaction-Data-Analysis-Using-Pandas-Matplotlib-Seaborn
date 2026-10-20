import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("c:/Users/Lenovo/Downloads/archive.zip")
print(df.head()) #output 5 rows fromm data
print(df.info()) #check metadata
print(df.isnull().sum())  #check missing values
df.drop_duplicates(inplace=True)
print(df.info())

#Data aggregation- groupby using pandas
transaction_summary=df.groupby("type").agg(
    total_amount=("amount","sum"),
    avg_amount=("amount","mean"),
    count_amount=("amount","count")
).reset_index()

print(transaction_summary)

#Visulization - bar plot, histogram, scatter plot
plt.figure(figsize=(10,6))
sns.barplot(x="type",y="total_amount",data=transaction_summary)
plt.title("Bankd data")
plt.show()


