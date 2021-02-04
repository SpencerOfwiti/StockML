import pandas as pd


def get_predictions(historical_data, prediction_data):
    history = pd.read_csv(historical_data)
    history = history[['Date', 'Price', 'Change %']]
    historical_values = list(zip(history['Date'], history['Price'], history['Change %']))
    predictions = pd.read_csv(prediction_data)
    prediction_values = [x for x in predictions['Prediction']]
    return historical_values, prediction_values
