def calculate_ratios(info):
    ratios = {
        "PE Ratio": info.get("trailingPE"),
        "ROE": info.get("returnOnEquity"),
        "ROA": info.get("returnOnAssets"),
        "Debt/Equity": info.get("debtToEquity"),
        "Profit Margin": info.get("profitMargins"),
        "Current Ratio": info.get("currentRatio")
    }
    return ratios