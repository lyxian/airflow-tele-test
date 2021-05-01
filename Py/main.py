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
    requests.get(url=domain)
    return 'Success...'

if __name__ == '__main__':
    print(getDateNow())