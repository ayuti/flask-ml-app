from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST': 
        try:
            market_cap = float(request.form['market_cap'])
            total_volume = float(request.form['total_volume'])
            features = pd.DataFrame([[market_cap, total_volume]], columns=['market_cap', 'total_volume'])
            prediction = model.predict(features)[0]
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)