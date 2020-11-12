from joblib import dump
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV

from src.scaling import scaler

# %% load train dataset
train = pd.read_csv('data/processed/Safaricom-Ltd(SCOM)-train.csv')

x_train = train.drop('Price', axis=1)
y_train = train['Price']

# %% scale the data
x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)

# %% use gridsearch to find the best parameter while implementing the KNN model
params = {'n_neighbors': [2, 3, 4, 5, 6, 7, 8, 9]}
knn = neighbors.KNeighborsRegressor()
model = GridSearchCV(knn, params, cv=5)
model.fit(x_train, y_train)

# %% save the model for later use
dump(model, 'models/knn/Safaricom-Ltd(SCOM).pkl')
