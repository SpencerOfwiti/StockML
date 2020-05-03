import pandas as pd
import pytest


@pytest.fixture
def processed_data():
	"""
	fixture holding processed dataset
	:return:
	"""
	data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')
	return data


def test_is_null_is_zero(processed_data):
	"""
	test if processed data has no null variables
	:param processed_data:
	:return:
	"""
	assert processed_data.isnull().sum().sum() == 0
