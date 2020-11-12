from joblib import load
import pandas as pd

from src.rmse import rms

# %% load test dataset
test = pd.read_csv('data/processed/Safaricom-Ltd(SCOM)-test.csv')
test = test['Price']

# %% load the Auto-ARIMA model
model = load('models/auto_arima/Safaricom-Ltd(SCOM).pkl')

# %% create predictions for the test data
pred = model.predict(test.shape[0])
pred = pd.DataFrame(pred, index=test.index, columns=['Predictions'])

# %% calculate RMSE
rms = rms(test, pred, 'Auto-ARIMA')
print('RMSE:', rms)

# %% create dataset with price and prediction
forecast = pd.DataFrame(index=range(0, len(test)), columns=['Price', 'Prediction'])

for i in range(0, len(test)):
    forecast['Price'][i] = test[i]
    forecast['Prediction'][i] = pred.values[i][0]

# %% save predicted data
forecast.to_csv('data/predicted/auto_arima/Safaricom-Ltd(SCOM).csv', index=False)
