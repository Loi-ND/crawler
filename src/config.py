import os
class GLobalConfig:
    API_KEY=None
    API_URL="https://api.massive.com/v3/reference/tickers"
    DATA_FOLDER="/kaggle/working/crawler/labels/data"
    INDEX_PATH="/kaggle/working/crawler/labels/index.txt"
    TICKERS_PATH="/kaggle/working/crawler/labels/tickers.json"

    def init(self):
        self.API_KEY = os.environ.get("API_KEY")
        with open(self.INDEX_PATH, mode="w") as file:
            index = os.environ.get("START_INDEX")
            file.write(str(index))
