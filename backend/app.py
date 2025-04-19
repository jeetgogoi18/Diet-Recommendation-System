from flask import Request, jsonify
import pickle
import numpy as np
import os

# Load the model once
model_path = os.path.join(os.path.dirname(__file__), '../model/diet_model.pkl')
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print("❌ Error loading model:", e)

def handler(request: Request):
    if request.method != "POST":
        return jsonify({"error": "Only POST method is allowed"}), 405

    try:
        data = request.get_json()
        print("📥 Received data:", data)

        # Mappings
        gender_map = {"Male": 0, "Female": 1}
        disease_map = {"Obesity": 0, "Diabetes": 1, "Hypertension": 2, "None": 3}
        activity_map = {"Active": 0, "Moderate": 1, "Sedentary": 2}
        allergy_map = {"peanuts": 0, "gluten": 1, "none": 2}

        # Extract and encode inputs
        gender = gender_map.get(data["Gender"], -1)
        disease = disease_map.get(data["Disease_Type"], -1)
        activity = activity_map.get(data["Physical_Activity_Level"], -1)
        allergy = allergy_map.get(data["Allergies"].lower(), -1)

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

        if -1 in features:
            return jsonify({"error": "Invalid input values"}), 400

        prediction = model.predict([features])[0]

        label_map = {0: "low carb", 1: "low sodium", 2: "balanced"}
        recommendation = label_map.get(int(prediction), "unknown")

        return jsonify({"recommendation": recommendation})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
