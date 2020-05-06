# Stock ML

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
* [Authors](#authors)
* [License](#license)
* [Acknowledgements](#acknowledgments)
* [Reports](#reports)

## Motivation

This project was born out of the need to make financial literacy and investment options available for the common citizen.
Over the years the number of individuals investing in the Kenyan Securities Market has reduced.
More and more of the trading is being done by investment companies and wealthy investors.
This provides a platform to lower the barriers to entry for everyone keen on investing in the securities market. 

## Build Status

[![Build Status](https://travis-ci.com/SpencerOfwiti/stock-ml.svg?token=u1WWyypPUJofJpbFsCQp&branch=master)](https://travis-ci.com/SpencerOfwiti/stock-ml)

## Built With
* [Python 3.6](https://www.python.org/) - The programming language used.
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framework used.
* [Travis CI](https://travis-ci.com/) - CI-CD tool used.

## Features

There is a lack of stock prices prediction especially in the Kenyan ecosystem.
We provide daily predictions on the stock price for the next day and an overview of what to expect in the coming week.

## Code Example

```
Give examples
```

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux systems
```
sudo apt-get install python3.6
```

Windows systems

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS
```
brew install python3
```

* **pip**

Linux or Mac OS
```
pip install -U pip
```

Windows systems
```
python -m pip install -U pip
```

## Installation

Set up virtual environment and install dependencies.

```
source setup.sh
```

Run python scripts.

```
python3 src/data/make_dataset.py
```

## Tests

This system uses pytest to run automated tests.
```
pytest
```

## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?label=Follow)](https://twitter.com/SpencerOfwiti)

See also the list of [contributors](https://github.com/SpencerOfwiti/stock-ml/contributors) who participated in this project.

[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/stock-ml)](https://github.com/SpencerOfwiti/stock-ml/contributors)

* **[Kelvin Minjire](https://github.com/Minjire)** - *Contributor*
* **[Kevin Wachira](https://github.com/wachira-kevin)** - *Contributor*

## License

This project is licensed under the GNU General Public License V3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Investing.com](https://www.investing.com/) from where the data was sourced.

## Reports

* [Processed dataset report](./reports/Processed-Safaricom-Report.html)
