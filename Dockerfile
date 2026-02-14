FROM python:3.10-slim

WORKDIR /app

COPY bot.py .

RUN pip install requests yfinance

CMD ["python", "bot.py"]