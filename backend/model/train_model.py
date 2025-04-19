import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("diet_recommendations_dataset.csv")

df=df.drop(["Patient_ID","BMI","Severity","Daily_Caloric_Intake","Cholesterol_mg/dL","Glucose_mg/dL","Dietary_Restrictions","Preferred_Cuisine","Weekly_Exercise_Hours","Adherence_to_Diet_Plan","Dietary_Nutrient_Imbalance_Score"], axis = 1)

# Encode categorical variables
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])
df['Disease_Type'] = encoder.fit_transform(df['Disease_Type'])
df['Physical_Activity_Level'] = encoder.fit_transform(df['Physical_Activity_Level'])
df['Allergies'] = encoder.fit_transform(df['Allergies'])
df['Diet_Recommendation'] = encoder.fit_transform(df['Diet_Recommendation'])

# Features and target
X = df.drop(columns=['Diet_Recommendation'])
y = df['Diet_Recommendation']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("diet_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
