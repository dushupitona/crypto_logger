from celery import shared_task
from crypto_logger.celery import app

from pybit.unified_trading import HTTP

from service.models import BTCUSD_info_model

import os

import datetime


@app.task
def collect_crypto():
    session = HTTP(
    testnet=False,
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET'),
    )

    response_data = session.get_tickers(
    category="inverse",
    symbol="BTCUSD",
    )
    
    data = response_data['result']['list'][0]

    data_date = datetime.datetime.fromtimestamp(response_data['time'] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    new_write = BTCUSD_info_model(
        log_date=str(data_date),
        last_price=data['lastPrice'],
        index_price=data['indexPrice'],
        mark_price=data['markPrice'],
        )
    
    new_write.save()

    print('New write !')
   