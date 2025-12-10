from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ''
    if request.method == 'POST':
        o2 = float(request.form['o2'])
        co = float(request.form['co'])
        nox = float(request.form['nox'])
        ch4 = float(request.form['ch4'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])

        data = pd.DataFrame([[o2, co, nox, ch4, temp, humidity]],
                            columns=['O2', 'CO', 'NOx', 'CH4', 'Temperature', 'Humidity'])
        prediction = model.predict(data)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
