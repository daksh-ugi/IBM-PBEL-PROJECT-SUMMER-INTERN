# ₹ Salary Predictor

A sleek and privacy-focused web app that provides instant salary estimates based on your profile. Powered by a trained machine learning model, it helps you benchmark your worth in today's job market with a clean, distraction-free black-and-white interface built using Streamlit.

---

## What Makes This App Stand Out

- **Instant, Intelligent Predictions:** See your estimated salary the moment you input your details—no waiting, no confusion.
- **Minimalist, Modern UI:** Enjoy a crisp, high-contrast glassmorphic design that puts your career front and center.
- **Full Privacy by Design:** All data processing happens locally in your browser. Your information stays with you, always.
- **Serious Machine Learning Power:** The app leverages XGBoost, one-hot encoded features, and sophisticated GridSearchCV tuning for predictions you can trust.
- **Thoughtful, Inspiring Experience:** Motivational quotes, smooth workflow, and a responsive form guide you through every step, inspiring confidence as you plan your next move.

---

## Project Structure

SalaryApp/
├── app.py # Streamlit UI & logic
├── model.pkl # Trained XGBoost model
├── features.pkl # Model features used for inference
├── salary.csv # (Optional) Training dataset
├── requirements.txt # Python dependencies
└── README.md # This file

text

---

## Getting Started

Follow these steps to get the app up and running on your local machine:

### 1. Clone the repository

git clone https://github.com/daksh-ugi/IBM-PBEL-PROJECT-SUMMER-INTERN.git


text

### 2. (Optional) Create and activate a virtual environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

### 3. Install the required packages

pip install -r requirements.txt

text

### 4. Run the app

streamlit run app.py

text

---

## How It Works

- Cleans and prepares your input data for use in prediction.
- Encodes all categorical fields dynamically using one-hot encoding.
- Utilizes a finely tuned XGBoost model (with GridSearchCV hyperparameter tuning) for reliable salary predictions.
- Compares your predicted salary against typical industry averages instantly.
- All model training and export details are available in the notebook file `PBEL.ipynb`.

---

## Requirements

- Python 3.x
- streamlit
- pandas
- scikit-learn
- xgboost
- joblib

You can install all dependencies via:

pip install -r requirements.txt

text

---

## Demo

<img width="1912" height="917" alt="Screenshot 2025-07-30 162040" src="https://github.com/user-attachments/assets/e26338bf-4700-4507-9a35-5966b38c315b" />
<br><br>
<img width="1919" height="928" alt="Screenshot 2025-07-30 162150" src="https://github.com/user-attachments/assets/27126449-fc0a-463c-b4ce-70c8ea82f597" />


---

## Motivation

> “Every pro was once an amateur. Every expert was once a beginner. So dream big and start now.”

---

## Credits

Developed with care by **Piyush Sharma**


