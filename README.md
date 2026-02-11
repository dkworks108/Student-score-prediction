# Student Score Prediction – End-to-End ML Project

This project is a comprehensive end-to-end Machine Learning web application designed to predict a student’s final exam score based on study habits and historical performance metrics.

The project encompasses:
* Data analysis and preprocessing
* Machine Learning model development
* Backend API development using Flask
* Frontend User Interface design
* Cloud deployment via Vercel

**Live Application URL:** [https://student-score-prediction-beta.vercel.app/ui](https://student-score-prediction-beta.vercel.app/ui)

---

## Problem Statement

The objective of this project is to provide an accurate prediction of a student's **exam score** by analyzing specific behavioral and academic inputs:
* Hours Studied
* Sleep Duration
* Attendance Percentage
* Previous Exam Results

---

## Dataset Description

The dataset consists of student records featuring the following attributes:

**Input Features:**
* `hours_studied`: Total number of hours dedicated to studying.
* `sleep_hours`: Average daily sleep duration.
* `attendance_percent`: Percentage of the classes attended.
* `previous_scores`: Numerical results from prior examinations.

**Target Variable:**
* `exam_score`: The predicted final exam score.

---

## Machine Learning Model

**Algorithm:** Multiple Linear Regression  
**Library:** scikit-learn  

### Methodology:
1.  **Data Ingestion:** Loading and cleaning the dataset.
2.  **Feature Engineering:** Separating independent variables (X) from the target variable (y).
3.  **Data Splitting:** Allocating 80% for training and 20% for testing.
4.  **Model Training:** Fitting the Multiple Linear Regression model to the training data.
5.  **Evaluation:** Measuring performance using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).
6.  **Serialization:** Saving the final model as `student_score_model.pkl`.

---

## Backend Architecture (Flask API)

The backend serves as the bridge between the trained model and the user interface.

### API Endpoints

#### 1. System Status
* **Method:** `GET`
* **Endpoint:** `/`
* **Description:** Confirms the API service is active.

#### 2. User Interface
* **Method:** `GET`
* **Endpoint:** `/ui`
* **Description:** Renders the frontend web application.

#### 3. Prediction Engine
* **Method:** `POST`
* **Endpoint:** `/predict`
* **Request Format (JSON):**
    ```json
    {
      "hours_studied": 6,
      "sleep_hours": 7,
      "attendance_percent": 85,
      "previous_scores": 70
    }
    ```
* **Response Format (JSON):**
    ```json
    {
      "predicted_exam_score": 37.8
    }
    ```

---

## Frontend Design

The interface is built with standard web technologies to ensure accessibility and speed:
* **HTML5 / CSS3:** Structured layout and responsive design.
* **JavaScript:** Logic for handling asynchronous API calls via the Fetch API.

### Key Features:
* Mobile-responsive layout for cross-device compatibility.
* Validation for input fields.
* Real-time result rendering.
* One-click reset functionality.

---

## Deployment

The application is hosted on **Vercel** utilizing Python serverless functions for optimized performance and scalability.

* **Architecture:** Serverless Flask backend.
* **Integration:** Unified domain for both frontend and backend assets.
* **Infrastructure:** No dedicated server management required.

---

## Project Structure

```text
Student-score-prediction/
│
├── api/
│   └── index.py             # Flask backend (Serverless entry point)
│
├── templates/
│   └── index.html           # Frontend User Interface
│
├── student_score_model.pkl   # Serialized ML model
├── requirements.txt         # Python library dependencies
├── vercel.json              # Vercel deployment configuration
└── README.md                # Project documentation
