from flask import Flask, render_template, request
import joblib
import numpy as np
import pickle

app = Flask(__name__)

# Load the saved model using pickle
with open('linear_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        floors = float(request.form['floors'])
        yr_built = float(request.form['yr_built'])

        # Prepare input for prediction
        input_data = np.array([[bedrooms, bathrooms, floors, yr_built]])
        predicted_price = model.predict(input_data)[0]

        return render_template('index.html', predicted_price=predicted_price)

    return render_template('index.html', predicted_price=None)

if __name__ == '__main__':
    app.run(debug=True)
