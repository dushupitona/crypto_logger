from celery import shared_task
from crypto_logger.celery import app

from pybit.unified_trading import HTTP

from service.models import BTCUSD_info_model

import os


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

    new_write = BTCUSD_info_model(
        last_price=data['lastPrice'],
        index_price=data['indexPrice'],
        mark_price=data['markPrice'],
        )
    
    new_write.save()

    print('New write !')   