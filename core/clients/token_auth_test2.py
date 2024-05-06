import requests
from pprint import pprint


# {'key': '45f40860bc1506edf7e8f62eeef9cf78ce8acfa7'}

def client():
    headers = {
        'Authorization': 'Token 45f40860bc1506edf7e8f62eeef9cf78ce8acfa7',
    }
    credentials = {
        'username': 'root',
        'password': 'root',
        'email': 'root@gmail.com',
    }
    response = requests.get('http://localhost:8000/api/kullanici-profilleri/', headers=headers)
    pprint(response.status_code)
    pprint(response.json())


if __name__ == '__main__':
    client()
