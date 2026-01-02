import logging
import time
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
from analytics-worker.config import Config

def get_logger(name: str, level: int = logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_config():
    return Config()

def get_timestamp():
    return int(time.time())

def get_datetime():
    return datetime.now(tzlocal())

def get_datetime_offset(offset: int):
    return get_datetime() - timedelta(minutes=offset)

def get_date():
    return datetime.now(tzlocal()).date()