import requests
from pprint import pprint


# {'key': '45f40860bc1506edf7e8f62eeef9cf78ce8acfa7'}

def client():
    credentials = {
        'username': 'armagandeneme',
        'password': 'root123.qw',
    }
    response = requests.post('http://127.0.0.1:8000/dj-rest-auth/login/', json=credentials)
    pprint(response.status_code)
    pprint(response.json())


if __name__ == '__main__':
    client()
