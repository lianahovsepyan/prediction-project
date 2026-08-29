import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/amankharwal/Website-data/main/tips.csv"
data = pd.read_csv(url)

data["sex"] = data["sex"].map({"Female": 0, "Male": 1})
data["smoker"] = data["smoker"].map({"No": 0, "Yes": 1})
data["day"] = data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
data["time"] = data["time"].map({"Sex": 0, "Dinner": 1, "Lunch": 0})

x = np.array(data[["total_bill", "sex", "smoker", "day", "time", "size"]])
y = np.array(data["tip"])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(xtrain, ytrain)

accuracy = model.score(xtest, ytest)
print(f"Model Accuracy (R^2 Score): {accuracy:.4f}")

features = np.array([[24.50, 1, 0, 3, 1, 3]])
predicted_tip = model.predict(features)
print(f"Predicted Tip: ${predicted_tip[0]:.2f}")
