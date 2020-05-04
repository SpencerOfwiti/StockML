import pandas as pd

# processed dataset
data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')


def check_null_values(data):
	"""
	check if processed data has no null variables
	:param data:
	:return:
	"""
	return data.isnull().sum().sum()


print(check_null_values(data))
