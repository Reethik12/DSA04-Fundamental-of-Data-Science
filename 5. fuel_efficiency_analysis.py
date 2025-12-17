import numpy as np

fuel_data=np.genfromtxt('Fuel_data.csv', delimiter=',', skip_header=1,dtype=str)

fuel_efficiency = fuel_data[:, 7].astype(float)
average_efficiency = np.mean(fuel_efficiency)
percentage_improvement=((fuel_efficiency[1]-fuel_efficiency[0])/fuel_efficiency[0])*100

print(f"Average Fuel Efficiency: {average_efficiency:.2f} MPG")
print(f"Percentage Improvement from First to Second Car: {percentage_improvement:.2f}%")