# Student Maths Score Predictor

This is an end-to-end machine learning project that predicts a student's math score based on various demographic and academic factors. The project is built with a modular structure, containerized with Docker, and deployed on AWS EC2 with Nginx and Gunicorn.

---

## 🚀 Live Demo

You can access the live web application here:

**[http://35.172.15.139](http://35.172.15.139)**

*Note: The application is hosted on an AWS EC2 instance. The link will only be active as long as the instance is running.*

---

## 📋 Features

* **Modular Code**: The project is structured into distinct components for data ingestion, transformation, and model training.
* **Web Interface**: A user-friendly web application built with Flask to input student data and receive real-time predictions.
* **Automated Training Pipeline**: A script to run the entire training process, from data ingestion to saving the final model.
* **Containerized Deployment**: The application is containerized using Docker for consistent and reliable deployment.
* **Cloud Hosted**: Deployed on an AWS EC2 instance with Nginx as a reverse proxy and Gunicorn as the application server.

---

## ⚙️ Technology Stack

* **Backend**: Python, Flask, Gunicorn
* **Machine Learning**: Scikit-learn, Pandas, NumPy
* **Deployment**: Docker, AWS EC2, Nginx
* **Experimentation**: Jupyter Notebook

---

## 🔧 Setup and Installation (Local)

To run this project on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/mlproject.git](https://github.com/your-username/mlproject.git)
cd mlproject
```

**2. Create and activate a virtual environment:**
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required dependencies:**
The `-e .` command installs your project in editable mode.
```bash
pip install -r requirements.txt
```

**4. Run the Flask application:**
```bash
python application.py
```
Navigate to `http://127.0.0.1:5000` in your web browser.

---

## 🐳 Running with Docker

You can also build and run the entire application using Docker.

**1. Build the Docker image:**
```bash
docker build -t mlproject .
```

**2. Run the Docker container:**
```bash
docker run -p 8000:8000 mlproject
```
Navigate to `http://localhost:8000` in your web browser.

---

## 📊 ML Pipeline Overview

The training process is broken down into three main stages:

1.  **Data Ingestion**: Reads the raw data, splits it into training and testing sets, and saves them in the `/artifacts` folder.
2.  **Data Transformation**: Applies preprocessing to the data, such as handling missing values, scaling numerical features, and one-hot encoding categorical features. It saves the preprocessor object as a pickle file.
3.  **Model Training**: Trains multiple regression models on the preprocessed data, uses GridSearchCV to find the best hyperparameters, and saves the best-performing model as a pickle file.
