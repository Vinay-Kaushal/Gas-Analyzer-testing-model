import joblib
import pandas as pd

model = joblib.load('model.pkl')

sample = pd.DataFrame([{
    'O2': 20.5,
    'CO': 60.0,
    'NOx': 80.0,
    'CH4': 2.5,
    'Temperature': 50,
    'Humidity': 60
}])

prediction = model.predict(sample)
print("Predicted Gas Type:", prediction[0])
