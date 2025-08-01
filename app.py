import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import traceback


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application

## route for a home page

@app.route("/", methods=["GET", "POST"])
def predict_datapoint():
    """
    GET request happens when the user firstt navigates to the page (to show the empty form to the users)
    POST requesr happens when the user submits the form (retriving the data, making predictions,
    sending the results back)
    """
    if request.method=="GET":
        return render_template("home.html")
    else:
        # this block run when the form is submitted by the user
        # retrive the data using 'name' attributes from the HTML(home.html) form
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # prepares the data and get a prediction
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)

        # send back results to the same page
        print("after Prediction")
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)


