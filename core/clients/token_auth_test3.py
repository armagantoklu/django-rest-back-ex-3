import requests
from pprint import pprint


# {'key': '45f40860bc1506edf7e8f62eeef9cf78ce8acfa7'}

def client():
    credentials = {
        'username': 'armagandeneme',
        'password1': 'root123.qw',
        'password2': 'root123.qw',
        'email': 'armagantoklu1@gmail.com',

    }
    response = requests.post('http://127.0.0.1:8000/dj-rest-auth/registration/', data=credentials)
    pprint(response)
    pprint(response.content)
    pprint(response.text)


if __name__ == '__main__':
    client()
