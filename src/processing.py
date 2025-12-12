import json
from pprint import pprint
from typing import List, Dict
from datetime import datetime

def check(params: List[Dict]) -> bool:
    for param in params:
        if param.get("ticker") == None or param.get("date") == None:
            return False
    return True
with open("../labels/stock-analystics.company_infos.json", mode="r", encoding="utf-8") as f:
    infos: List[Dict] = json.load(f)
    tickers = set()
    params = []
    for info in infos:
        ticker = info.get("ticker", None)
        if ticker and ticker not in tickers:
            tickers.add(ticker)
            timestamp = info.get("time_update")
            date = str(datetime.fromtimestamp(timestamp).date())
            params.append({"ticker": ticker,
                          "date": date})
    lenght = len(params)
    tickers = {}
    tickers["Thinh"] = params[:(lenght//2)]
    tickers["Loi"] = params[(lenght//2):]
    with open("../labels/tickers.json", mode="w") as file:
        json.dump(tickers, file, indent=4)
