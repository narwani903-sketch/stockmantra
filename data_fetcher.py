import yfinance as yf
import pandas as pd

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    return stock.info

def get_financials(symbol):
    stock = yf.Ticker(symbol)
    return {
        "income": stock.financials,
        "balance": stock.balance_sheet,
        "cashflow": stock.cashflow
    }

def get_price_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1y")

def get_shareholding_pattern():
    # Placeholder (real promoter data requires paid APIs)
    data = {
        "Promoters": 52.3,
        "FIIs": 18.2,
        "DIIs": 12.5,
        "Public": 17.0
    }
    return pd.DataFrame(list(data.items()), columns=["Category", "Holding %"])