from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder="../templates")

# Load model safely
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "..", "student_score_model.pkl")

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return "Student Score Prediction API is running"


@app.route("/ui")
def ui():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_data = np.array([[
            float(data["hours_studied"]),
            float(data["sleep_hours"]),
            float(data["attendance_percent"]),
            float(data["previous_scores"])
        ]])

        prediction = model.predict(input_data)

        return jsonify({
            "predicted_exam_score": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400
