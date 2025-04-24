from sklearn.linear_model import LinearRegression
dataset = {
    "experience": [2, 3, 7],
    "salary": [45000, 55000, 100000]
}

x = [[value] for value in dataset["experience"]]
y = dataset["salary"]
model = LinearRegression()
model.fit(x, y)

predicted_price = model.predict([[20000]])
print(predicted_price)  # Predicted price for a house with 2000 sqft
    