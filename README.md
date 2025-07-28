# 🎓 Student Maths Score Predictor

This project predicts a student's math score based on various demographic and academic factors. It follows a modular design, leverages Docker for containerization, and is hosted on an AWS EC2 instance using Nginx and Gunicorn for production deployment.

---

## 🌐 Live Demo

You can access the live web application here:

**🔗 [http://35.172.15.139](http://35.172.15.139)**

> ⚠️ **Note:** The application is hosted on an AWS EC2 instance. The link will only work while the instance is running.

---

## 🚀 Features

- **🧩 Modular Code**: The project is divided into separate components for data ingestion, transformation, and model training.
- **🖥 Web Interface**: A simple Flask web app allows users to input student data and get real-time predictions.
- **⚙️ Automated Training Pipeline**: A single script runs the full pipeline—from raw data ingestion to saving the final model.
- **🐳 Containerized Deployment**: Uses Docker for consistent deployment across environments.
- **☁️ Cloud Hosted**: Deployed on AWS EC2 with Nginx as a reverse proxy and Gunicorn as the WSGI server.

---

## 🛠 Technology Stack

| Layer            | Tools & Libraries                     |
|------------------|----------------------------------------|
| **Backend**      | Python, Flask, Gunicorn                |
| **Machine Learning** | Scikit-learn, Pandas, NumPy         |
| **Deployment**   | Docker, AWS EC2, Nginx                 |
| **Experimentation** | Jupyter Notebook                    |

---

## 🧪 ML Pipeline Overview

### 1. 📥 Data Ingestion
- Reads raw CSV data.
- Splits it into training and test sets.
- Saves both datasets to the `/artifacts` folder.

### 2. 🔧 Data Transformation
- Handles missing values.
- Scales numerical features.
- Applies one-hot encoding to categorical features.
- Saves the transformation pipeline as a `.pkl` (pickle) file.

### 3. 🧠 Model Training
- Trains multiple regression models.
- Uses `GridSearchCV` for hyperparameter tuning.
- Selects the best model based on performance.
- Saves the final model as a pickle file for inference.

---

## 📁 Project Structure

