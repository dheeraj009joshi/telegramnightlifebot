import requests
import time
response=[]
lat=19.1176
long= 72.9060
results=[]
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{long}&opennow=true&type=Bar&keyword=nightlife&key=AIzaSyCE7Ba4LoGrJcSlgMo3K9M0sAdvmUmDiIc&rankby=distance"
res = requests.request("GET", url)
for t in res.json()['results']:
    response.append(t)
next=(res.json())['next_page_token']
print(next)
time.sleep(2)
for i in range(4):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{long}&opennow=true&type=Bar&keyword=nightlife&key=AIzaSyCE7Ba4LoGrJcSlgMo3K9M0sAdvmUmDiIc&rankby=distance&pagetoken={next}"
    res = requests.request("GET", url)
    print(res.json())
    for t in res.json()['results']:
        response.append(t)
    if 'next_page_token' in res.text:
        next=(res.json())['next_page_token']
        print(next)

        time.sleep(2)
    else:
        break
print(len(response))
