# From https://docs.python.org/ko/3/howto/logging.html
import logging

# logging.basicConfig(level=logging.DEBUG, format='[%(levelname)1.1s][%(asctime)s.%(msecs)03d][%(name)-8.8s][%(filename)s:Ln %(lineno)d] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG, format='[%(levelname)1.1s][%(asctime)s.%(msecs)03d] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)1.1s][%(asctime)s.%(msecs)03d] %(message)s', datefmt="%y/%m/%d %H:%M:%S")

console = logging.StreamHandler()
file_hanler = logging.FileHandler(filename="test.log")

console.setLevel(logging.INFO)
file_hanler.setLevel(logging.DEBUG)

console.setFormatter(formatter)
file_hanler.setFormatter(formatter)

logger.addHandler(console)
#logger.addHandler(file_hanler)

#logger.setLevel(level=logging.WARN)
logger.debug('This message does not appear')
#logger.setLevel(level=logging.INFO)
logger.info('This message should appear on the console again')