import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

API_ID = CONFIG.getint('account', 'api_id')
API_HASH = CONFIG.get('account', 'api_hash')
USERNAME = CONFIG.get('account', 'username')
PHONE = CONFIG.get('account', 'phone')
PASSWORD = CONFIG.get('account', 'password') if CONFIG.get('account', 'password') else None  # Проверка на пустое значение

CHANNEL_ID = CONFIG.get('account', 'channel_id')
CHANNEL_2_ID = CONFIG.get('account', 'channel_2_id')