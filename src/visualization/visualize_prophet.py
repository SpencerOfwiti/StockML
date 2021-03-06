import matplotlib.pyplot as plt
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('..')
from threshold import get_threshold

# %% load datasets
test = pd.read_csv('../../data/predicted/prophet/Safaricom-Ltd(SCOM).csv')
data = pd.read_csv('../../data/processed/Safaricom-Ltd(SCOM).csv')

threshold = get_threshold(data)
test.index = data[threshold:].index

# %% plot and save price prediction
plt.plot(data['Price'], label='Actual Price')
plt.plot(test['Prediction'], label='Predicted Price')
plt.xlabel('Time (Days)')
plt.ylabel('Share Price (KSh.)')
plt.title('Safaricom Price Prediction (Prophet)')
plt.legend()
plt.savefig('../../reports/figures/Safaricom_prophet.png')
plt.show()
