import json
import requests

#user_url = "http://api.quotable.io/quotes/-CzNrWMGIg8V"
user_url = input("Put your url below \n")
response = requests.get(user_url)
data = response.json()
print(data)
#if response.status_code == 200 and "Quote" in data:
if response.status_code == 200 and "Quote" in data:
    print('success')
    print(data)

else:
    print('Invalid quote resource!')
