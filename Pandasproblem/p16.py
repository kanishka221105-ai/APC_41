# 16. Dataset: weather.csv
# Columns: Date,City,Temperature,Humidity,Rainfall
# Problem Statement: Read the CSV file and:
# Find the maximum temperature. 
# Find the minimum temperature. 
# Calculate the average temperature. 
# Display records where temperature is above 35°C. 
# Calculate city-wise average temperature.
import pandas as pd
import os
folder_path = r'C:\Users\KANISHKA\OneDrive\Desktop\python sem 5\Pandasproblem'
file_path = os.path.join(folder_path, 'weather.csv')

if not os.path.exists(file_path):
    sample_data = {
        'Date': ['2026-06-01', '2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03'],
        'City': ['Kolhapur', 'Pune', 'Kolhapur', 'Mumbai', 'Pune'],
        'Temperature': [34.5, 36.0, 33.0, 35.5, 37.2],
        'Humidity': [65, 55, 70, 80, 50],
        'Rainfall': [0.0, 2.5, 1.2, 5.0, 0.0]
    }
    pd.DataFrame(sample_data).to_csv('weather.csv', index=False)

df = pd.read_csv('weather.csv')

print("Maximum temperature:", df['Temperature'].max())
print("Minimum temperature:", df['Temperature'].min())
print("Average temperature:", df['Temperature'].mean())
print("\nRecords where temperature is above 35°C:\n", df[df['Temperature'] > 35])
print("\nCity-wise average temperature:\n", df.groupby('City')['Temperature'].mean())