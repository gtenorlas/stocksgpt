# pip install requests
# pip install python-dotenv
# pip install pandas
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()


stock_api_key = os.environ.get('ALPHA_VANTAGE')
if stock_api_key is None:
    print('ALPHA_VANTAGE is not set in .env file')

symbol = 'AAPL'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={stock_api_key}'

response = requests.get(url)
data = response.json()
#print (data)


#use pandas to analyze data received and use matplotlib to plot the data
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df = df[['4. close']].astype(float)

""" plt.plot(df.index, df['4. close'])
plt.title('AAPL Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
 """
