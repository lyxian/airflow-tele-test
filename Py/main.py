import logging

from datetime import datetime
import requests
import pytz

def getDateNow():
    return datetime(
        datetime.now().year,
        datetime.now().month,
        datetime.now().day,
        0,
        0,
        0,
        tzinfo=pytz.timezone('Asia/Singapore')
        )

def test():
    print('Printing...')
    return 'Returning...'
    
def start():
    domain = 'https://yxian-carousell.herokuapp.com/start'
    requests.get(url=domain, params={'source': 'Airflow'})
    return 'Success...'

def live():
    try:
        msg = f'Logging at {datetime.now()}...'
        logging.info(msg)

        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')

        if datetime.now().minute >= 55: 
            domain = 'https://yxian-carousell.herokuapp.com/'
            response = requests.get(url=domain)
            logging.info(f'Received {response.status_code} response...')

        return 'Success...'
    except:
            return 'Failed...'


if __name__ == '__main__':
    print(getDateNow())