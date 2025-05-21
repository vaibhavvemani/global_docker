from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split

import pandas as pd
import pickle

data = pd.read_csv("housing_data.csv")
X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

with open("custom_model.pkl", "wb") as f:
    pickle.dump(model, f)