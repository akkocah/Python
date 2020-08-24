
import requests, json
api_url = 'https://api.binance.com/api/v3/ticker/price?symbol='

coin = input("Whic coin do you buy enter 'ETHUSDT' for etherium, 'BTCUSDT' for Bitcoin  : ")
count_of_coin = int(input(f"How many {coin} will you buy : "))

result = requests.get(api_url+coin)
result = result.json()
#result = json.loads(result.text)  Bir üst satırdaki komut yerine buda yazılıyor.
print(result, "\n")
print(f"{result['symbol']} price is =  ${round(float(result['price']),2):,}\n")
print(f"{count_of_coin} {coin} price is = ${round((float(result['price'])*count_of_coin),2):,}\n")
