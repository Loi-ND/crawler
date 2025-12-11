from config import GLobalConfig
import os

GLobalConfig.init(GLobalConfig)
print(f"API_KEY: {GLobalConfig.API_KEY}")
print(f"Start index: {os.environ.get("INDEX")}")