from joblib import dump
import pandas as pd
from pmdarima import auto_arima

# %% load train dataset
train = pd.read_csv('../../data/processed/Safaricom-Ltd(SCOM)-train.csv')
train = train['Price']

# %% implement the Auto-ARIMA model
model = auto_arima(train, start_p=1, start_q=1, max_p=3, max_q=3, m=12, start_P=0, seasonal=True, d=1, D=1,
                   trace=True, error_action='ignore', suppress_warnings=True)

# %% save the model for later use
dump(model, '../../models/auto_arima/Safaricom-Ltd(SCOM).pkl')
