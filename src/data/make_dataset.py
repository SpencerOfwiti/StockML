import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('..')
from report import generate_report

plt.rcParams['figure.figsize'] = (12, 8)

#%% create a dataframe
data = pd.read_csv('../../data/raw/Safaricom-Ltd(SCOM).csv')
data = data[:-2]  # remove rows displaying statistics
print(data.tail())
print(data.shape)
print(data.describe())

#%% generate report
profile = generate_report(data, 'Raw Safaricom Data Report')
profile.to_file(output_file='../../reports/Raw-Safaricom-Report.html')

#%% show number of missing data per column
null_counts = data.isnull().sum()
print('Number of null values in each column:\n', null_counts)

#%% show datatypes in dataset
print('Data types and their frequency:\n', data.dtypes.value_counts())

# show datatypes for each column
data_dtypes = pd.DataFrame(data.dtypes, columns=['dtypes'])
print(data_dtypes)

#%% convert incorrectly mapped columns to float
cols = ['Price', 'Open', 'High', 'Low']
for col in cols:
	data[col] = data[col].astype('float')


#%% convert volume traded from object to float
def convert_vol(val):
	if val.endswith('M'):
		val = float(val[:-1]) * 1000000
	elif val.endswith('K'):
		val = float(val[:-1]) * 1000
	return val


data['Vol.'] = data['Vol.'].apply(convert_vol)

#%% changing the format of Date column
months = {
	'Jan': 1,
	'Feb': 2,
	'Mar': 3,
	'Apr': 4,
	'May': 5,
	'Jun': 6,
	'Jul': 7,
	'Aug': 8,
	'Sep': 9,
	'Oct': 10,
	'Nov': 11,
	'Dec': 12
}


def convert_date(val):
	val = val.split(' ')
	month = months[val[0]]
	day = val[1].strip(',')
	year = val[2]
	date = f'{year}-{month:02d}-{day}'
	return date


data['Date'] = pd.to_datetime(data['Date'].apply(convert_date), format='%Y-%m-%d')

#%% generate report
profile = generate_report(data, 'Interim Safaricom Data Report')
profile.to_file(output_file='../../reports/Interim-Safaricom-Report.html')

#%% save cleaned data
print(data.head())
print(data.info())
print(data.shape)
data.to_csv('../../data/interim/Safaricom-Ltd(SCOM).csv', index=False)
