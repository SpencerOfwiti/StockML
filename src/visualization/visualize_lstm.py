import pandas as pd
import matplotlib.pyplot as plt
from src.threshold import get_threshold

# %% load datasets
test = pd.read_csv('data/predicted/lstm/Safaricom-Ltd(SCOM).csv')
data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')

threshold = get_threshold(data)
test.index = data[threshold:].index

# %% plot and save price prediction
period = 60  # 2 months
plt.plot(data['Price'][-period:], label='Actual Price')
plt.plot(test['Prediction'], label='Predicted Price')
plt.xlabel('Time (Days)')
plt.ylabel('Share Price (KSh.)')
plt.title('Safaricom Price Prediction (LSTM)')
plt.legend()
plt.savefig('reports/figures/Safaricom_lstm.png')
plt.show()
