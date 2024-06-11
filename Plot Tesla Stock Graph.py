import matplotlib.pyplot as plt
import yfinance as yf

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], color='blue', linewidth=2, label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Extract Tesla stock data
tesla_data = yf.download('TSLA')

# Plot the graph
make_graph(tesla_data, title='Tesla Stock Price')
