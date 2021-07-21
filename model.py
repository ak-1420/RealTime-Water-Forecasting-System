import dill as pickle 

def model(reservoir_name , prediction_input):
    
    #for serializing

    #import pandas and numpy
    import pandas as pd
    import numpy as np

    #load dataset

    reservoir_dataset = pd.read_csv('reservoir_dataset_cleaned.csv')

    #get constant columns

    constant_columns = []

    normal_columns = []

    for col in reservoir_dataset:

        if(len(reservoir_dataset[col].unique()) == 1):

            constant_columns.append(col)
        elif col != 'Date':
            normal_columns.append(col)
    
    #print(constant_columns)
    #print(normal_columns)


    reservoir_dataset.drop(constant_columns , axis = 1 , inplace = True)

    #import sktim libs

    reservoir_timeseries = reservoir_dataset[reservoir_name]

    reservoir_dataset['Date'] = pd.to_datetime(reservoir_dataset['Date'])

    from sktime.forecasting.model_selection import temporal_train_test_split

    y_train , y_test = temporal_train_test_split(reservoir_timeseries , test_size = 365)

    from sktime.forecasting.naive import NaiveForecaster
    from sktime.forecasting.base import ForecastingHorizon

    fh = ForecastingHorizon(y_test.index , is_relative = False)

    forecaster = NaiveForecaster(strategy = 'last' ,sp = 365)

    forecaster.fit(y_train)

    y_pred = forecaster.predict(fh)


    from sktime.performance_metrics.forecasting import mean_absolute_percentage_error

    print('mean_error:',mean_absolute_percentage_error(y_test , y_pred)) 

    prediction_result = forecaster.predict(prediction_input)

    return prediction_result


import numpy as np

res_name = 'Mahi Bajaj Sagar'
pred_inp = np.arange(7688 , 7688 + 365 + 1)


# pred_op = model(res_name , pred_inp)

# print(pred_op)



#serialize the model

pickle.dump(model , open('predictor.pkl','wb'))

mdl = pickle.load(open('predictor.pkl','rb'))

pred_op = mdl(res_name,pred_inp)

print(pred_op)




