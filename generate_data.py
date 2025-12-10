import pandas as pd
import numpy as np

n = 1000

data = {
    'O2': np.round(np.random.uniform(18.0, 21.0, n), 2),
    'CO': np.round(np.random.uniform(0, 100, n), 2),
    'NOx': np.round(np.random.uniform(0, 200, n), 2),
    'CH4': np.round(np.random.uniform(0, 5, n), 2),
    'Temperature': np.round(np.random.uniform(20, 70, n), 1),
    'Humidity': np.round(np.random.uniform(30, 90, n), 1)
}

df = pd.DataFrame(data)

def label_row(row):
    if row['CO'] > 50:
        return 'CO Leak'
    elif row['NOx'] > 100:
        return 'NOx High'
    elif row['O2'] < 19.0:
        return 'O2 Low'
    else:
        return 'Normal'

df['Gas_Type'] = df.apply(label_row, axis=1)
df.to_csv('gas_data.csv', index=False)

print("✅ Data saved to gas_data.csv")
