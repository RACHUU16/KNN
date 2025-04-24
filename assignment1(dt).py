from sklearn.tree import DecisionTreeClassifier

# Training data: [Number of Appliances, Hours of Usage], Energy Efficient? (1=Yes, 0=No)
data = [[10, 5], [15, 9], [8, 4], [20, 10], [12, 6]]
labels = [1, 0, 1, 0, 1]

# Train a Decision Tree Classifier
model = DecisionTreeClassifier(criterion="gini")
model.fit(data, labels)

# Predict for a new household
new_household = [[14, 7]]  # Example: 14 appliances, 7 hours/day usage
prediction = model.predict(new_household)

print("Prediction (1=Efficient, 0=Not Efficient):", prediction[0])
