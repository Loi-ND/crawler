from config import (INDEX_PATH, 
                    DATA_FOLDER, 
                    TICKERS_PATH, 
                    API_URL, 
                    API_KEY)
import time
import os
from typing import Dict, List, Tuple
import json
import requests
from pprint import pprint
def get_index() -> int:
    index = None
    with open(INDEX_PATH, mode="r") as file:
        index = file.read()
        index = int(index)
    return index

def save_index(index: int):
    with open(INDEX_PATH, mode="w") as file:
        file.write(str(index))

def save_result(index: int, ticker: str, result: Dict):
    path = os.path.join(DATA_FOLDER, str(index) + "_" + ticker + ".json")
    with open(path, mode="w") as file:
        json.dump(result, file, indent=4)
    print(f"Saved result to {path}")

def get_tickers(task_owner: str="Loi"):
    with open(TICKERS_PATH, mode="r") as file:
        data: Dict = json.load(file)
        tickers = data.get(task_owner)
    index = get_index()
    return index, tickers[index:]

def pull_data():
    index, list_params = get_tickers()
    for idx, params in enumerate(list_params):
        try:
            ticker = params.get("ticker")
            params = {"date": params.get("date")}
            params.update({"apiKey": API_KEY})
            headers = {
                "Content-Type": "application/json"
            }
            url = API_URL+f"/{ticker}"

            res: Dict = requests.get(url=url, 
                                    headers=headers, 
                                    params=params).json()
            result = res.get("results")
            save_result(index=idx+index, ticker=ticker, result=result)
            save_index(index=idx+1+index)
        except Exception as e:
            print(f"Error while fetching data -> {e}")
        time.sleep(13)