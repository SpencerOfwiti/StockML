# Stock ML 

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 
![GitHub repo size](https://img.shields.io/github/repo-size/SpencerOfwiti/stock-ml.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

Implementation of stock market price prediction of various Kenyan companies' shares including Safaricom e.t.c.
It utilizes various Machine Learning algorithms such as Long Short Term Memory(LSTM), Prophet and Auto-Regressive Intergrated Moving Average(ARIMA).
It bases it's analysis on historical trading data dating back more than five years. 

## Table of contents
* [Motivation](#motivation)
* [Build Status](#build-status)
* [Built With](#built-with)
* [Features](#features)
* [Code Example](#code-example)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Tests](#tests)
* [Deployment](#deployment)
* [Contributions](#contributions)
* [Bug / Feature Request](#bug--feature-request)
* [Authors](#authors)
* [License](#license)
* [Acknowledgements](#acknowledgments)
* [Reports](#reports)

## Motivation

This project was born out of the need to make financial literacy and investment options available for the common citizen.
Over the years the number of individuals investing in the Kenyan Securities Market has reduced.
More and more of the trading is being done by investment companies and wealthy investors.
This provides a platform to lower the barriers to entry for everyone keen on investing in the securities market. 
It provides daily predictions on the stock price for the next day and an overview of what to expect in the coming week.

## Build Status

[![Build Status](https://travis-ci.com/SpencerOfwiti/stock-ml.svg?token=u1WWyypPUJofJpbFsCQp&branch=master)](https://travis-ci.com/SpencerOfwiti/stock-ml)

## Built With
* [Python 3.6](https://www.python.org/) - The programming language used.
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framework used.
* [Travis CI](https://travis-ci.com/) - CI-CD tool used.

## Features

- Aggregate daily stock closing price.
- Exploration and cleaning of companies' stock prices data.
- Application of machine learning algorithms in stock price prediction.
- Visualization of stock price predictions.

## Code Example

```python
def check_null_values(data):
	"""
	check if processed data has no null variables
	:param data:
	:return:
	"""
	return data.isnull().sum().sum()


print(check_null_values(data))
```

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux:
```
sudo apt-get install python3.6
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

## Installation

Clone this repository:
```
git clone https://github.com/SpencerOfwiti/stock-ml
```

To set up virtual environment and install dependencies:
```
source setup.sh
```

To run python scripts:
```
python3 src/data/make_dataset.py
```

## Tests

This system uses pytest to run automated tests.

To run automated tests:
```
pytest
```

## Deployment

Add additional notes about how to deploy this on a live system

## Contributions

To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/SpencerOfwiti/stock-ml/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/SpencerOfwiti/stock-ml/issues/new). Please include sample queries and their corresponding results.

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

See also the list of [contributors](https://github.com/SpencerOfwiti/stock-ml/contributors) who participated in this project.

[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/stock-ml.svg)](https://github.com/SpencerOfwiti/stock-ml/contributors)

* **[Kelvin Minjire](https://github.com/Minjire)** - *Contributor*
* **[Kevin Wachira](https://github.com/wachira-kevin)** - *Contributor*

## License

This project is licensed under the GNU General Public License V3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Investing.com](https://www.investing.com/) from where the data was sourced.

## Reports

* [Processed dataset report](./reports/Processed-Safaricom-Report.html)
