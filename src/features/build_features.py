import sys
import pandas as pd
from fastai.tabular.transform import add_datepart

from src.report import generate_report
from src.threshold import get_threshold

# %% load dataset
data = pd.read_csv('data/interim/Safaricom-Ltd(SCOM).csv')
data.index = data['Date']

# %% sort data in ascending order
data = data.sort_index(ascending=True, axis=0)

# %% create dataset with date and the target variable
new_data = pd.DataFrame(index=range(0, len(data)), columns=['Date', 'Price'])

for i in range(0, len(data)):
    new_data['Date'][i] = data['Date'][i]
    new_data['Price'][i] = data['Price'][i]

# %% create date features
add_datepart(new_data, 'Date')
new_data.drop('Elapsed', axis=1, inplace=True)

# %% distinguishing mondays and fridays from other dates
new_data['mon_fri'] = 0
for i in range(0, len(new_data)):
    if new_data['Dayofweek'][i] == 0 or new_data['Dayofweek'][i] == 4:
        new_data['mon_fri'] = 1
    else:
        new_data['mon_fri'] = 0

#%% generate report
profile = generate_report(new_data, 'Processed Safaricom Data Report')
profile.to_file(output_file='reports/Processed-Safaricom-Report.html')

# %% save processed data
print(new_data.head())
print(new_data.info())
print(new_data.shape)
new_data.to_csv('data/processed/Safaricom-Ltd(SCOM).csv', index=False)

# %% splitting data into train and test data at 80% train
threshold = get_threshold(new_data)
train = new_data[:threshold]
test = new_data[threshold:]

# %% save train and test data
print(train.shape)
print(test.shape)
train.to_csv('data/processed/Safaricom-Ltd(SCOM)-train.csv', index=False)
test.to_csv('data/processed/Safaricom-Ltd(SCOM)-test.csv', index=False)
