import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url="http://127.0.0.1:5001"
response=requests.get(url=url,headers=headers)
print(response.headers)
print(response.text)