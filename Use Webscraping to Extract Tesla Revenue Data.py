import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate and extract data
    revenue_data = []

    # Find the table containing revenue data
    revenue_table = soup.find('table', class_='revenue-table')

    # Check if the table is found
    if revenue_table:
        # Extract data from table rows
        for row in revenue_table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 2:  # Ensure there are at least two columns
                revenue_data.append([cols[0].text.strip(), cols[1].text.strip()])

        # Create DataFrame
        tesla_revenue = pd.DataFrame(revenue_data, columns=['Date', 'Revenue'])

        # Display the last five rows
        print(tesla_revenue.tail())
    else:
        print("Revenue table not found on the webpage.")
else:
    print("Failed to retrieve data from the webpage. Status code:", response.status_code)
