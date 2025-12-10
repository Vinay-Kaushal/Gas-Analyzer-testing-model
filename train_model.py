import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('gas_data.csv')

X = df[['O2', 'CO', 'NOx', 'CH4', 'Temperature', 'Humidity']]
y = df['Gas_Type'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")
