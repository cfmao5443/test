import requests
import yfinance as yf
from datetime import datetime

# Settings
TELEGRAM_TOKEN = "8344989956:AAEgD5NyWL3rd3-z_PNQKVWCdDWzg-HQX3M"
CHAT_ID = "8361467288"

#  ZROZ price
zroz = yf.Ticker("ZROZ")
zroz_price = zroz.history(period="1d")["Close"].iloc[-1]

# Find 30Y Treasury 
# Yahoo Finance 30Y Treasury: "^TYX" 
# 
ty30 = yf.Ticker("^TYX")  
last_price = ty30.history(period="1d")["Close"].iloc[-1]
yield_30 = last_price / 100  

# Sending Telegram 
message = f"""
Report
Date: {datetime.now().strftime("%Y-%m-%d")}

ZROZ: ${zroz_price:.2f}

"""

send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
requests.post(send_url, data={"chat_id": CHAT_ID, "text": message})

print("Sent successfully")