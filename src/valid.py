import glob
import os
from pprint import pprint
import json
from typing import Dict

folder = "../labels/data"
json_files = glob.glob(os.path.join(folder, "*.json"))

list_obj = []
tickers = []
for link in json_files:
    with open(link, mode="r") as file:
        obj: Dict = json.load(file)
        if obj != None:
            list_obj.append(obj)
            ticker = obj.get("ticker")
            tickers.append(ticker)

pprint(len(tickers))
