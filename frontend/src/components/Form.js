import React, { useState } from "react";
import axios from "axios";

const Form = () => {
  const [formData, setFormData] = useState({
    Gender: "",
    Age: "",
    Weight_kg: "",
    Height_cm: "",
    Disease_Type: "",
    Physical_Activity_Level: "",
    Blood_Pressure_mmHg: "",
    Allergies: "",
  });

  const [recommendation, setRecommendation] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", formData);
      setRecommendation(response.data.recommendation); // ✅ fixed key name
    } catch (error) {
      console.error("Prediction failed:", error);
      setRecommendation("Error occurred while fetching recommendation.");
    }
  };

  const dietMap = {
    0: "Low-Carb Diet",
    1: "Mediterranean Diet",
    2: "High-Protein Diet",
    3: "DASH Diet",
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <select name="Gender" onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>

        <input type="number" name="Age" placeholder="Age" onChange={handleChange} />
        <input type="number" name="Weight_kg" placeholder="Weight (kg)" onChange={handleChange} />
        <input type="number" name="Height_cm" placeholder="Height (cm)" onChange={handleChange} />

        <select name="Disease_Type" onChange={handleChange}>
          <option value="">Select Disease</option>
          <option value="Obesity">Obesity</option>
          <option value="Diabetes">Diabetes</option>
          <option value="Hypertension">Hypertension</option>
          <option value="None">None</option>
        </select>

        <select name="Physical_Activity_Level" onChange={handleChange}>
          <option value="">Select Physical Activity</option>
          <option value="Active">Active</option>
          <option value="Moderate">Moderate</option>
          <option value="Sedentary">Sedentary</option>
        </select>

        <input
          type="number"
          name="Blood_Pressure_mmHg"
          placeholder="Blood Pressure"
          onChange={handleChange}
        />

        <select name="Allergies" onChange={handleChange}>
          <option value="">Select Allergies</option>
          <option value="Peanuts">Peanuts</option>
          <option value="Gluten">Gluten</option>
          <option value="None">None</option>
        </select>

        <button type="submit">Submit</button>
      </form>

      {recommendation !== null && (
        <div>
          <h3>
            Recommended Diet Plan:{" "}
            {dietMap[recommendation] || recommendation}
          </h3>
        </div>
      )}
    </div>
  );
};

export default Form;
