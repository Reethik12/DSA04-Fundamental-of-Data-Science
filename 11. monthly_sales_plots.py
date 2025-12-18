import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Sales_data.csv')

df["Month_sales"]=pd.to_datetime(df["Month_sales"])
monthly_sales=df.groupby("Month_sales")["Total"].sum()

plt.plot(monthly_sales.index,monthly_sales.values,marker='o')
plt.title("Monthly Sales Trend (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

plt.scatter(monthly_sales.index,monthly_sales.values)
plt.title("Monthly Sales Distribution (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()