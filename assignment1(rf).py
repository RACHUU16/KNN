# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Training data: [Attendance Frequency (days/week), Age], Renewed Membership? (1=Yes, 0=No)
data = np.array([[3, 25], [1, 45], [4, 30], [0, 50], [5, 28], [2, 35]])
labels = np.array([1, 0, 1, 0, 1, 0])  # 1=Renewed, 0=Did not renew

# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42)

# Train the model on the data
model.fit(data, labels)

# Predict on new data
new_customer = np.array([[3, 40]])  # Example: 3 days/week attendance, 40 years old
prediction = model.predict(new_customer)

# Display the result
print("Prediction (1=Renewed, 0=Did Not Renew):", prediction[0])
