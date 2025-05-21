import pickle 
import numpy as np
with open("custom_model.pkl", "rb") as f:
    global model
    model = pickle.load(f)

test_data = np.array([[1900]])
result = model.predict(test_data)
print(result[0].item())