from joblib import load
import pandas as pd
import numpy as np

from src.rmse import rms
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
inputs = data[len(data) - len(test) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

x_test = []
for i in range(60, inputs.shape[0]):
    x_test.append(inputs[i-60: i, 0])
x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)

# %% calculate RMSE
rms = rms(test, predicted_price, 'LSTM')
print('RMSE:', rms)

# %% create dataset with price and prediction
pred = pd.DataFrame(index=range(0, len(test)), columns=['Price', 'Prediction'])

for i in range(0, len(test)):
    pred['Price'][i] = test[i][0]
    pred['Prediction'][i] = predicted_price[i][0]

# %% save predicted data
pred.to_csv('data/predicted/lstm/Safaricom-Ltd(SCOM).csv', index=False)
