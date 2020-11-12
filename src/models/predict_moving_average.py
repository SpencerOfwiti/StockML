import pandas as pd

from src.rmse import rms
from src.threshold import get_overflow

# %% load dataset
train = pd.read_csv('data/processed/Safaricom-Ltd(SCOM)-train.csv')
test = pd.read_csv('data/processed/Safaricom-Ltd(SCOM)-test.csv')
data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')

# %% create predictions for test data
pred = []
overflow = get_overflow(data)
for i in range(0, test.shape[0]):
    a = train['Price'][len(train) - overflow + i:].sum() + sum(pred)
    b = a / overflow
    pred.append(b)

# %% calculate RMSE
rms = rms(test['Price'], pred, 'Moving Average')
print('RMSE:', rms)

# %% trim dataset to price and prediction
test['Prediction'] = pred
test = test[['Price', 'Prediction']]

# %% save predicted data
test.to_csv('data/predicted/moving_average/Safaricom-Ltd(SCOM).csv', index=False)
