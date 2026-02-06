from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model ONCE
model = joblib.load("student_score_model.pkl")


# Home route (sanity check)
@app.route("/", methods=["GET"])
def home():
    return "Student Score Prediction API is running"


# Health check route
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200


# UI route (FRONTEND)
@app.route("/home", methods=["GET"])
def ui():
    return render_template("index.html")


# Remove favicon 404 error
@app.route("/favicon.ico")
def favicon():
    return "", 204


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        required_fields = [
            "hours_studied",
            "sleep_hours",
            "attendance_percent",
            "previous_scores"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"Missing field: {field}"
                }), 400

        # Convert inputs
        hours_studied = float(data["hours_studied"])
        sleep_hours = float(data["sleep_hours"])
        attendance_percent = float(data["attendance_percent"])
        previous_scores = float(data["previous_scores"])

        # Prepare model input (2D array)
        input_data = np.array([[
            hours_studied,
            sleep_hours,
            attendance_percent,
            previous_scores
        ]])

        prediction = model.predict(input_data)

        return jsonify({
            "predicted_exam_score": round(float(prediction[0]), 2)
        }), 200

    except ValueError:
        return jsonify({
            "error": "Invalid input type. Numbers required."
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# Run server (ALWAYS LAST)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
