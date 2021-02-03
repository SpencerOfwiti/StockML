import csv
import numpy as np


def rms(actual, prediction, model):
    rmse = np.sqrt(np.mean(np.power((np.array(actual)-np.array(prediction)), 2)))
    data = [[model, rmse]]

    file = open('data/report/rmse.csv', 'a+', newline='')

    with file:
        write = csv.writer(file)
        write.writerows(data)

    return rmse
