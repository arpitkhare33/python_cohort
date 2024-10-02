# ============================================== Python Basics: Final Project =======================================
import requests


def write_stock_data_to_excel(stock_data, file_name='stock_market_data.csv'):
    with open(file_name, 'w') as file: # block based file opening and closing approach
        file.write("Date,Open,High,Low,Close,Volume\n")

        for date, data in stock_data.items():
            row = f"{date},{data['1. open']},{data['2. high']},{data['3. low']},{data['4. close']},{data['5. volume']}\n"
            file.write(row)
        print(f"Stock Market data for the company Tesla has been saved in the file {file_name}")


api_key = open("api_key.txt", 'r').read()
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=' + api_key
r = requests.get(url)
data = r.json()
time_series_data = data['Time Series (Daily)']
print(time_series_data)
write_stock_data_to_excel(time_series_data)


