from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained Random Forest model
try:
    with open("model/diet_model.pkl", "rb") as f:
        model = pickle.load(f)
        print(" Model loaded successfully.")
except Exception as e:
    print(" Error loading model:", e)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("📥 Received data:", data)

        # Mapping for categorical inputs
        gender_map = {"Male": 0, "Female": 1}
        disease_map = {"Obesity": 0, "Diabetes": 1, "Hypertension": 2, "None": 3}
        activity_map = {"Active": 0, "Moderate": 1, "Sedentary": 2}
        allergy_map = {"peanuts": 0, "gluten": 1, "none": 2}

        # Use correct keys based on frontend data
        gender = gender_map.get(data["Gender"], -1)
        disease = disease_map.get(data["Disease_Type"], -1)
        activity = activity_map.get(data["Physical_Activity_Level"], -1)
        allergy = allergy_map.get(data["Allergies"].lower(), -1)  # normalize casing

        features = [
            gender,
            int(data["Age"]),
            int(data["Weight_kg"]),
            int(data["Height_cm"]),
            disease,
            activity,
            int(data["Blood_Pressure_mmHg"]),
            allergy
        ]

        print("🔢 Encoded features:", features)

        if -1 in features:
            return jsonify({"error": "Invalid input values"}), 400

        prediction = model.predict([features])[0]
        print("✅ Prediction:", prediction)

        # Map predicted number back to diet label
        label_map = {0: "low carb", 1: "low sodium", 2: "balanced"}
        recommendation = label_map.get(int(prediction), "unknown")

        return jsonify({"recommendation": recommendation})


    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
