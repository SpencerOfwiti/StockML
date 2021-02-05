import pandas as pd


def get_predictions(historical_data, prediction_data):
    history = pd.read_csv(historical_data)
    history = history[['Date', 'Price', 'Change %']]
    historical_values = list(zip(history['Date'], history['Price'], history['Change %']))
    historical_values = [{hist[0]: hist[1]} for hist in historical_values]
    predictions = pd.read_csv(prediction_data)
    prediction_values = list(zip(history['Date'], predictions['Prediction'][::-1]))
    prediction_values = [{pred[0]: pred[1]} for pred in prediction_values]
    return historical_values, prediction_values
