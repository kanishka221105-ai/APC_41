# 4. Create a dictionary containing:
# Patient ID
# Patient Name
# Age
# Disease
# Medical Charges
# Convert the dictionary into a DataFrame and:
# Display patients above 60 years. 
# Find the average medical charge. 
# Find the maximum medical charge. 
# Display patients whose medical charges are greater than ₹50,000. 
import pandas as pd

data = {
    'Patient ID': [1, 2, 3, 4],
    'Patient Name': ['Sam', 'Ravi', 'Anita', 'John'],
    'Age': [65, 45, 62, 50],
    'Disease': ['Diabetes', 'Flu', 'Hypertension', 'Cardiac'],
    'Medical Charges': [40000, 15000, 60000, 75000]
}
df = pd.DataFrame(data)

print("Patients above 60 years:\n", df[df['Age'] > 60])
print("\nAverage Medical Charge:", df['Medical Charges'].mean())
print("Maximum Medical Charge:", df['Medical Charges'].max())
print("\nPatients with medical charges > ₹50,000:\n", df[df['Medical Charges'] > 50000])