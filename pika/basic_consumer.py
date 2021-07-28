import os
import logging
import configparser
import pika

logging.basicConfig(level=logging.DEBUG, format='[%(levelname) 1.1s][%(asctime)s.%(msecs)03d] %(message)s', datefmt='%y/%m/%d %H:%M:%S')

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

def main():
    credentials = pika.PlainCredentials(
        config['RABBIT']['ACCOUNT'], 
        config['RABBIT']['PASSWORD'])
    parameters = pika.ConnectionParameters(
        host=config['RABBIT']['IP'], 
        port=config['RABBIT']['PORT'], 
        virtual_host=config['RABBIT']['VIRTUAL_HOST'], 
        credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)