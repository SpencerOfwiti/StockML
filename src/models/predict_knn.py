import sys
from joblib import load
import pandas as pd

sys.path.append('..')
from scaling import scaler
from rmse import rms

# %% load test dataset
test = pd.read_csv('../../data/processed/Safaricom-Ltd(SCOM)-test.csv')

x_test = test.drop('Price', axis=1)
y_test = test['Price']

# %% scale the data
x_test_scaled = scaler.fit_transform(x_test)
x_test = pd.DataFrame(x_test_scaled)

# %% load the KNN model
model = load('../../models/knn/Safaricom-Ltd(SCOM).pkl')

# %% create predictions for test data
pred = model.predict(x_test)

# %% calculate RMSE
rms = rms(y_test, pred, 'KNN')
print('RMSE:', rms)

# %% trim dataset to price and prediction
test['Prediction'] = pred
test = test[['Price', 'Prediction']]

# %% save predicted data
test.to_csv('../../data/predicted/knn/Safaricom-Ltd(SCOM).csv', index=False)
