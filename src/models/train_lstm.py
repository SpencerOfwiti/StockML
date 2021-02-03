from joblib import dump
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

from src.threshold import get_threshold
from src.scaling import scaler

# %% load dataset
data = pd.read_csv('data/interim/Safaricom-Ltd(SCOM).csv')
data = data[['Date', 'Price']]
data.index = data['Date']
data.drop('Date', axis=1, inplace=True)

# %% sort data in ascending order
data = data.sort_index(ascending=True, axis=0)

# %% save dataset for later use
data.to_csv('data/processed/Safaricom-Ltd(SCOM)-lstm.csv', index=False)

# %% split data into train data
data_list = data.values
# threshold = get_threshold(data_list)
train = data_list

# %% scale the data
scaled_data = scaler.fit_transform(data_list)

# convert data to x_train and y_train
x_train, y_train = [], []
for i in range(60, len(train)):
    x_train.append(scaled_data[i-60: i, 0])
    y_train.append(scaled_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# %% implement the LSTM network
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

# %% compile and fit the model
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=30, batch_size=1, verbose=2)

# %% save model for later use
dump(model, 'models/lstm/Safaricom-Ltd(SCOM).pkl')
