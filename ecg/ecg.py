import pandas as pd
import numpy as np

# Parameters for the dataset
num_samples = 1000

# Generate synthetic data
data = {
    "Age": np.random.randint(30, 80, size=num_samples),  # Age between 30 and 80
    "Gender": np.random.choice(['Male', 'Female', 'Other'], size=num_samples),
    "CP": np.random.randint(0, 4, size=num_samples),  # Chest Pain Type (0-3)
    "Trestbps": np.random.randint(90, 200, size=num_samples),  # Resting Blood Pressure (90-200 mmHg)
    "Chol": np.random.randint(150, 400, size=num_samples),  # Serum Cholesterol (150-400 mg/dl)
    "Fbs": np.random.choice([0, 1], size=num_samples),  # Fasting Blood Sugar (0 or 1)
    "Restecg": np.random.randint(0, 3, size=num_samples),  # Resting ECG Result (0-2)
    "Thalach": np.random.randint(60, 200, size=num_samples),  # Maximum Heart Rate Achieved (60-200 bpm)
    "Exang": np.random.choice([0, 1], size=num_samples),  # Exercise Induced Angina (0 or 1)
    "Oldpeak": np.random.uniform(0.0, 6.0, size=num_samples),  # Oldpeak (0.0 to 6.0)
    "Slope": np.random.randint(0, 3, size=num_samples),  # Slope (0-2)
    "Ca": np.random.randint(0, 4, size=num_samples),  # Number of Major Vessels (0-3)
    "Thal": np.random.randint(0, 4, size=num_samples),  # Thalassemia (0-3)
}

# Randomly assign diagnosis based on conditions
data['Diagnosis'] = np.where(
    (data['CP'] == 2) | (data['Thalach'] < 100) | (data['Oldpeak'] > 2.0) | (data['Chol'] > 240), 
    'Heart Disease', 
    'No Heart Disease'
)

# Create a DataFrame
ecg_df = pd.DataFrame(data)

# Save to CSV
ecg_df.to_csv('synthetic_ecg_data.csv', index=False)
print("Synthetic ECG dataset generated: synthetic_ecg_data.csv")
