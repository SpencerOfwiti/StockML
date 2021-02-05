import pandas as pd


def get_predictions(historical_data, prediction_data):
    history = pd.read_csv(historical_data)
    history = history[['Date', 'Price', 'Change %']]
    historical_values = list(zip(history['Date'], history['Price'], history['Change %']))
    historical_values = [{'Date': hist[0], 'Price': hist[1], '% Change': hist[2]} for hist in historical_values]
    predictions = pd.read_csv(prediction_data)
    prediction_values = list(zip(history['Date'], predictions['Prediction'][::-1]))
    prediction_values = [{'Date': pred[0], 'Price': pred[1]} for pred in prediction_values]
    return historical_values, prediction_values
