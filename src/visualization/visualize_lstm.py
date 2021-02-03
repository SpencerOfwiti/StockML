import sys
import pandas as pd
import matplotlib.pyplot as plt

# %% load datasets
test = pd.read_csv('data/predicted/lstm/Safaricom-Ltd(SCOM).csv')
data = pd.read_csv('data/processed/Safaricom-Ltd(SCOM).csv')

start_index = len(data) - 1
last_price = data.iloc[start_index].Price
top_row = pd.DataFrame({'Prediction': [last_price]})
test = pd.concat([top_row, test]).reset_index(drop=True)
test.index = [counter for counter in range(start_index, start_index + len(test))]

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
