from joblib import load
import pandas as pd
import numpy as np

from src.scaling import scaler
from src.threshold import get_threshold

# %% load dataset
data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM)-lstm.csv')

# %% load the LSTM model
model = load('models/lstm/Safaricom-Ltd(SCOM).pkl')

# %% split data into test data
data_list = data.values
threshold = get_threshold(data_list)
test = data_list[threshold:, :]

# %% scale the data
scaled_data = scaler.fit_transform(data_list)

# %% create predictions for test data
inputs = data[len(data) - 60:].values


def make_prediction(test_data):
    test_data = np.reshape(test_data, (test_data.shape[0], test_data.shape[1], 1))
    predicted = model.predict(test_data)
    predicted = scaler.inverse_transform(predicted)
    return predicted


days = 5
predicted_price = []
for _ in range(days):
    loop_inputs = np.append(inputs, np.array(inputs), axis=0)
    loop_inputs = loop_inputs.reshape(-1, 1)
    loop_inputs = scaler.transform(loop_inputs)

    x_test = []
    for i in range(60, loop_inputs.shape[0]):
        x_test.append(loop_inputs[i - 60: i, 0])
    x_test = np.array(x_test)
    predicted_price = make_prediction(x_test)
    inputs = np.append(inputs, np.array([predicted_price[-1]]), axis=0)

# %% create dataset with price and prediction
pred = pd.DataFrame(index=range(0, len(predicted_price)), columns=['Prediction'])

for i in range(0, len(predicted_price)):
    pred['Prediction'][i] = predicted_price[i][0]

# %% save predicted data
pred.to_csv('data/predicted/lstm/Safaricom-Ltd(SCOM).csv', index=False)
