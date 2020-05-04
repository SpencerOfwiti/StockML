import pandas as pd
import pytest
from ..dataset_completeness import check_null_values


@pytest.fixture
def data():
	"""
	fixture holding processed dataset
	:return:
	"""
	data = pd.read_csv('src/tests/fixtures/test.csv')
	return data


def test_is_null_is_zero(data):
	"""
	test if processed data has no null variables
	:param data:
	:return:
	"""
	assert check_null_values(data) == 0
