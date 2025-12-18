import pandas as pd

df=pd.read_csv("customer_sales_data.csv")

df["Purchase_DATE"] = pd.to_datetime(df["Purchase_DATE"], format="%d.%m.%y")
df["Month_Year"] = df["Purchase_DATE"].dt.strftime("%B %Y")
past_month = df[df["Month_Year"] == "November 2021"]
age_frequency = past_month["Age"].value_counts()

print("Customer Age Frequency in Past month (November 2021):")
print(age_frequency)