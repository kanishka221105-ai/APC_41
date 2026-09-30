# 15. Dataset: patients.csv
# Columns: Patient_ID,Name,Age,Gender,Disease,Medical_Expense
# Problem Statement: Read the CSV file and:
# Display patients above 60 years. 
# Calculate average medical expense. 
# Find the patient with the highest medical expense. 
# Count patients for each disease. 
# Display patients whose medical expense exceeds ₹50,000.
import pandas as pd
import os
folder_path = r'C:\Users\KANISHKA\OneDrive\Desktop\python sem 5\Pandasproblem'
file_path = os.path.join(folder_path, 'patients.csv')  # (or employees.csv, etc.)

if not os.path.exists(file_path):
    sample_data = {
        'Patient_ID': [1, 2, 3, 4, 5],
        'Name': ['Ramesh', 'Suman', 'Kiran', 'Anita', 'Sunil'],
        'Age': [65, 45, 70, 52, 62],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Disease': ['Diabetes', 'Hypertension', 'Diabetes', 'Asthma', 'Hypertension'],
        'Medical_Expense': [45000, 30000, 55000, 48000, 60000]
    }
    pd.DataFrame(sample_data).to_csv('patients.csv', index=False)

df = pd.read_csv('patients.csv')

print("Patients above 60 years:\n", df[df['Age'] > 60])
print("\nAverage medical expense:", df['Medical_Expense'].mean())

highest_expense_patient = df.loc[df['Medical_Expense'].idxmax()]
print("\nPatient with the highest medical expense:\n", highest_expense_patient)

print("\nPatient count for each disease:\n", df['Disease'].value_counts())
print("\nPatients whose medical expense exceeds ₹50,000:\n", df[df['Medical_Expense'] > 50000])