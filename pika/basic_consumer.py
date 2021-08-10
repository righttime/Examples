import os
import logging
import configparser
import pika
import time
from threading import Thread

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)1.1s][%(asctime)s.%(msecs)03d] %(message)s', datefmt="%y/%m/%d %H:%M:%S")
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

credentials = pika.PlainCredentials(
    config['RABBIT']['ACCOUNT'], 
    config['RABBIT']['PASSWORD'])
parameters = pika.ConnectionParameters(
    host=config['RABBIT']['IP'], 
    port=config['RABBIT']['PORT'], 
    virtual_host=config['RABBIT']['VIRTUAL_HOST'], 
    credentials=credentials)


class Publisher(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.connection = None
        self.channel = None

    def run(self):
        logger.info('Run Publisher')
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare('test')
        self.channel.basic_publish(
            exchange='test_exchange',
            routing_key='test',
            body='test message body',
            properties=pika.BasicProperties(
                content_type='text/plain',
                content_encoding='utf8',
                delivery_mode=1
            )
        )
        self.connection.close()
        pass



class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.connection = None
        self.channel = None

    def run(self):
        logger.info('Run Consumer')
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare('test')
        self.channel.basic_consume('test', self.on_message)
        self.channel.start_consuming()

    def on_message(self, channel, method_frame, header_frame, body):
        logger.info(channel)
        logger.info(method_frame)
        logger.info(header_frame)
        logger.info(body)

    def stop(self):
        self.channel.stop_consuming()



def main():
    #connection = pika.BlockingConnection(parameters=parameters)    
    #channel = connection.channel()
    th_p = Publisher()
    th_c = Consumer()

    th_c.start()
    th_p.start()
    th_p.join()
    time.sleep(5)
    th_c.stop()
    logger.info("Finished")


main()