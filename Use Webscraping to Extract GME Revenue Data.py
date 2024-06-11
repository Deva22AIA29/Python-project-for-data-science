import yfinance as yf
import pandas as pd

# Extract GameStop (GME) stock data
gme_data = yf.download('GME')

# Reset the index
gme_data.reset_index(inplace=True)

# Save to CSV
gme_data.to_csv('gme_stock_data.csv', index=False)

# Display the first five rows
print(gme_data.head())
