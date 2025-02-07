import yfinance as yf

# Extract Tesla stock data
tesla_data = yf.download('TSLA')

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print(tesla_data.head())
