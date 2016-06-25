import http.client
import json
import requests
import time


print("hello there")
apikey="e0eae31cb11d510cf0aab8818f18acb0954e6c08"
venue="SKLEX"
ticker="BFI"

base_url = "https://api.stockfighter.io/ob/api"

account = "BM44074201"

quant_desired=100000

client_price=2837

order = {
  "account": account,
  "venue": venue,
  "symbol": ticker,
  "price": client_price,  
  "qty": 100,
  "direction": "buy",
  
    
  "orderType": "limit"
}

dump_order=json.dumps(order)

header= {"X-Starfighter-Authorization":apikey
    
}


quote_order={
    "venue": venue,
    "stock": ticker
    
}


dump_quote_order=json.dumps(quote_order)



cx=0

while (cx< 1000):
    


    r=requests.post(base_url + '/venues/'+venue+'/stocks/'+ticker+'/orders', data=dump_order, headers=header)
    print(r.text)
    print("sent a order in for 100")

    time.sleep(3)
    cx+=1



    
    
'''

r=requests.post(base_url + '/venues/'+venue+'/stocks/'+ticker+'/orders', data=dump_order, headers=header)


print("here is the response")
print(r)
print(r.text)



print("hearto beat status")
hearto = requests.get("https://api.stockfighter.io/ob/api/heartbeat")

print(hearto)
'''


'''
connection = http.client.HTTPSConnection("api.stockfighter.io/ob/api/venues/IUWDEX/stocks/PLH/orders")

headers = {'X-Starfighter-Authorization': apikey}

#change to include the orders information


json_foo = json.dumps(order)

connection.request('POST', '/markdown', json_foo, headers)

response = connection.getresponse()
print(response.read().decode())

'''

