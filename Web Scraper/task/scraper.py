import requests

def Scraper():
    user_url = input("Give your url")
    response = requests.get(user_url)
    if response.headers['status-code'] == 200:
        print('success')
        return response.json()
    else:
        print('conection failed')
