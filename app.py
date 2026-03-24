from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
data = pd.read_csv("./cleaned_data.csv")
pipe = pickle.load(open("RidgeModeluttam.pkl", "rb"))

@app.route('/')
def index():
    locations = sorted(data["location"].dropna().unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # --- Get values ---
        location = request.form.get('location', '').strip()
        bhk_raw  = request.form.get('BHK', '').strip()
        bath_raw = request.form.get('bath', '').strip()
        sqft_raw = request.form.get('total_sqft', '').strip()

        # --- Check empty fields ---
        missing = []
        if not location:   missing.append("Location")
        if not bhk_raw:    missing.append("BHK")
        if not bath_raw:   missing.append("Bathrooms")
        if not sqft_raw:   missing.append("Square Feet")

        if missing:
            return f"Please fill in: {', '.join(missing)}", 400

        # --- Convert to numbers ---
        try:
            bhk = float(bhk_raw)
        except ValueError:
            return "BHK must be a valid number (e.g. 2 or 3)", 400

        try:
            bath = float(bath_raw)
        except ValueError:
            return "Bathrooms must be a valid number (e.g. 1 or 2)", 400

        try:
            sqft = float(sqft_raw)
        except ValueError:
            return "Square Feet must be a valid number (e.g. 1200)", 400

        # --- Logical validations ---
        if bhk <= 0 or bhk > 20:
            return "BHK must be between 1 and 20", 400

        if bath <= 0 or bath > 20:
            return "Bathrooms must be between 1 and 20", 400

        if sqft < 100:
            return "Square Feet seems too low. Please enter a valid area (min 100)", 400

        if sqft > 100000:
            return "Square Feet seems too high. Please enter a realistic value", 400

        if bath > bhk + 2:
            return "Bathrooms count seems unusually high for the given BHK", 400

        # --- Predict ---
        input_df = pd.DataFrame(
            [[location, sqft, bath, bhk]],
            columns=['location', 'total_sqft', 'bath', 'BHK']
        )
        prediction = pipe.predict(input_df)[0] * 1e5

        if prediction <= 0:
            return "Could not generate a valid prediction. Please check your inputs", 400

        return str(np.round(prediction, 2))

    except Exception as e:
        return f"Something went wrong: {str(e)}", 500

import os
if __name__ == "__main__":
    app.run(debug=False, port=int(os.environ.get("PORT", 5001)))