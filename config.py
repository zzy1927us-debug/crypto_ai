import os
from dotenv import load_dotenv

# Load .env file for environment variables
load_dotenv()

# Load configuration from environment variables
# Comma-separated lists for symbols and exchanges
SYMBOLS = os.getenv("SYMBOLS", "BTCUSDT,ETHUSDT,BNBUSDT").split(",")
EXCHANGES = os.getenv("EXCHANGES", "Binance,OKX").split(",")

# Path to save reports
REPORT_PATH = os.getenv("REPORT_PATH", os.path.expanduser("~/MarketReports"))

# DeepSeek API key
DEEPC_API_KEY = os.getenv("DEEPC_API_KEY")

# Days of historical data to fetch
DAYS_HISTORY = int(os.getenv("DAYS_HISTORY", "30"))
