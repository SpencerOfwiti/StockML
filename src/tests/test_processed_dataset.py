import pandas as pd

data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')


def test_is_null_is_zero():
	assert data.isnull().sum().sum() == 0
