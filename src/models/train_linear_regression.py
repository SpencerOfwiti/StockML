import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

# %% load train dataset
train = pd.read_csv('../../data/processed/Safaricom-Ltd(SCOM)-train.csv')

x_train = train.drop('Price', axis=1)
y_train = train['Price']

# %% implement the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# %% save model for later use
dump(model, '../../models/linear_regression/Safaricom-Ltd(SCOM).pkl')
