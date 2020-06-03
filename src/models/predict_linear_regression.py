import sys
import pandas as pd
from joblib import load

sys.path.append('..')
from rmse import rms

# %% load test dataset
test = pd.read_csv('../../data/processed/Safaricom-Ltd(SCOM)-test.csv')

x_test = test.drop('Price', axis=1)
y_test = test['Price']

# %% load the linear regression model
model = load('../../models/linear_regression/Safaricom-Ltd(SCOM).pkl')

# %% create predictions for test data
pred = model.predict(x_test)

# %% calculate RMSE
rms = rms(y_test, pred, 'Linear Regression')
print('RMSE:', rms)

# %% trim dataset to price and prediction
test['Prediction'] = pred
test = test[['Price', 'Prediction']]

# %% save predicted data
test.to_csv('../../data/predicted/linear_regression/Safaricom-Ltd(SCOM).csv', index=False)
