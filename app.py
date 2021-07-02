#improt flask

from logging import debug
from flask import Flask , render_template , request
from datetime import date
import numpy as np
import joblib
import pandas as pd

#create an instance of Flask

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rainfall')
def rainfall():
    return render_template('rainfall.html')

@app.route('/reservoirs')
def reservoirs():
    return render_template('reservoirs.html')


@app.route('/forecast_rainfall',methods=['GET','POST'])
def forecast_rainfall():
    
    days_to_forecast = request.form['rainfall_days']  

    start_date = date(2021,1,1)
    end_date =  date.today()
    
    total_days = days_between_dates(start_date , end_date)

    total_days = int(total_days) + int(days_to_forecast)


    date_labels = pd.date_range(start_date, periods=total_days + 1).strftime("%d-%m-%Y ").tolist()

    
    # convert entered days into feedable data
    # i.e to convert as numpy array
    prediction_input = preprocess(7672,total_days)

    # now predict with the reservoir_model
    rainfall_forecaster = joblib.load(open("rainfall_model.pkl","rb"))
    
    #predict

    prediction_result = rainfall_forecaster.predict(prediction_input)

    labels = date_labels
    values = prediction_result.tolist()

    #actual values we need
    labels = labels[-(int(days_to_forecast)):]
    values = values[-(int(days_to_forecast)):]


    return render_template('rainfall.html',labels = labels , values = values)



@app.route('/forecast_reservoir',methods=['GET','POST'])
def forecast_reservoir():

    days_to_forecast = request.form['reservoir_days']  

    start_date = date(2021,1,1)
    end_date =  date.today()
    
    total_days = days_between_dates(start_date , end_date)

    total_days = int(total_days) + int(days_to_forecast)

    date_labels = pd.date_range(start_date, periods=total_days + 1).strftime("%d-%m-%Y ").tolist()
    
    prediction_input = preprocess(7688,total_days)

    # now predict with the reservoir_model
    reservoir_forecaster = joblib.load(open("reservoir_model.pkl","rb"))
    
    #predict

    prediction_result = reservoir_forecaster.predict(prediction_input)



    labels = date_labels
    values = prediction_result.tolist()

    #actual values we need
    labels = labels[-(int(days_to_forecast)):]
    values = values[-(int(days_to_forecast)):]

    return render_template('reservoirs.html',labels = labels , values = values)



@app.route('/about')
def about():
    return render_template('about.html')



def days_between_dates(d0 , d1):
    delta = d1 - d0
    return delta.days

def preprocess(last_number,total_days):

    data = np.arange(last_number , last_number + total_days + 1)

    return data

if __name__ == '__main__':
    app.run()