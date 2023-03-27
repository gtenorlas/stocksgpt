import requests
from dotenv import load_dotenv
import os

load_dotenv()


stock_api_key = os.environ.get('ALPHA_VANTAGE')
if stock_api_key is None:
    print('ALPHA_VANTAGE is not set in .env file')

symbol = 'AAPL'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={stock_api_key}'

response = requests.get(url)
data = response.json()
//print (data)
