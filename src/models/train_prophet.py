import sys
import pandas as pd
from fbprophet import Prophet

sys.path.append('..')
from threshold import get_threshold
from rmse import rms

# %% load dataset
new_data = pd.read_csv('../../data/interim/Safaricom-Ltd(SCOM).csv')
new_data = new_data[['Date', 'Price']]
new_data.index = new_data['Date']

# %% sort data in ascending order
new_data = new_data.sort_index(ascending=True, axis=0)
new_data.rename(columns={'Price': 'y', 'Date': 'ds'}, inplace=True)

# %% split data into train and test data
threshold = get_threshold(new_data)
train = new_data[:threshold]
test = new_data[threshold:]

# %% implement the Prophet model
model = Prophet()
model.fit(train)

# %% save train and test data
train.to_csv('../../data/processed/Safaricom-Ltd(SCOM)-prophet-train.csv', index=False)
test.to_csv('../../data/processed/Safaricom-Ltd(SCOM)-prophet-test.csv', index=False)

# %% create predictions for the test data
close_prices = model.make_future_dataframe(periods=len(test))
forecast = model.predict(close_prices)

# %% calculate RMSE
forecast_test = forecast['yhat'][threshold:]
rms = rms(test['y'], forecast_test, 'Prophet')
print('RMSE:', rms)

# %% trim dataset to price and prediction
test['Prediction'] = forecast_test.values
test = test[['y', 'Prediction']]

# %% save predicted data
test.to_csv('../../data/predicted/prophet/Safaricom-Ltd(SCOM).csv', index=False)
