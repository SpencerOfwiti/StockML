import pandas as pd


def get_predictions(file):
    predictions = pd.read_csv(file)
    preds = [x for x in predictions['Prediction']]
    return preds
