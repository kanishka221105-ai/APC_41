#Read a student.csv file using pandas and display the first five and last five recors
import pandas as pd
df = pd.read_csv("student.csv")
print("----- First 5 Records -----")
print(df.head())
print("\n----- Last 5 Records -----")
print(df.tail())

