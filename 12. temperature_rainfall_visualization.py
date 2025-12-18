import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Temp_and_rain.csv')

monthly_temp=df.groupby("Month")["Temp"].mean()
monthly_rain=df.groupby("Month")["rain"].mean()

plt.plot(monthly_temp.index,monthly_temp.values,marker='o')
plt.title("Average Monthly Temperature (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.show()

plt.scatter(monthly_rain.index,monthly_rain.values)
plt.title("Average Monthly Rainfall (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Average Rainfall")
plt.show()