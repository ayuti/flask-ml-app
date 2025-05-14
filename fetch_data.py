import requests
import pandas as pd

def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd",
               "order": "market_cap_desc", 
               "per_page": 10,
                 "page": 1,                        
                "sparkline": "false"
               }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data)[['id', 'symbol', 'market_cap', 'total_volume', 'current_price']]
        df.to_csv("data.csv", index=False)
        print("Data saved to data.csv")
    else:
        print("Error:", response.status_code, response.json())
    # return df

if __name__ == "__main__":
    fetch_data()