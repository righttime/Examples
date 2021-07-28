import os
import logging
from dotenv import load_dotenv
import configparser

logging.basicConfig(level=logging.DEBUG, format='[%(levelname) 1.1s][%(asctime)s.%(msecs)03d] %(message)s', datefmt='%y/%m/%d %H:%M:%S')

if 0:
    load_dotenv()   

    RABBIT_IP = os.environ.get('RABBIT_IP')
    RABBIT_PORT = os.environ.get('RABBIT_PORT')
    RABBIT_VIRTUAL_HOST = os.environ.get('RABBIT_VIRTUAL_HOST')
    RABBIT_ACCOUNT = os.environ.get('RABBIT_ACCOUNT')
    RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD')
    logging.info(RABBIT_IP)
else:
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    for key in config['DEFAULT']:
        logging.info(f'{key:20s} : {config["DEFAULT"][key]}')