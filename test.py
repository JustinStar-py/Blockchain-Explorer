# import math
# import requests
# from requests import sessions
# from decimal import Decimal
# url = "https://apilist.tronscan.org/api/account?address=TRUVJMsYwcGZL5ywSf4dR6A89Br9UwiZLP"
import asyncio
from bs4 import BeautifulSoup

# a= -1
# with requests.Session() as session:
#        response = session.get(url).json()

# for i in response["tokenBalances"]:
#     a += 1
#     s = "0" * response["tokenBalances"][a]["tokenDecimal"]
#     l = int(f"1{s}")
#     b = float(response["tokenBalances"][a]["balance"])
#     our_value = Decimal(b/l)
#     print(our_value)

from os import name, path
import requests,time,aiohttp
from requests.sessions import Session, session

directory = r'C:\Users\Hamidreza\Desktop\logos'

names = []
url="https://api.coingecko.com/api/v3/coins/list"
resp = requests.get(url).json()
start_num = int(input("Start Number? "))
for coin in resp[start_num:len(resp)]:
    if len(coin["name"]) <= 15: 
    #    print(coin["name"].replace(" ","-"))
       names.append(coin["name"].replace(" ","-"))
       
async def tasks():
        for count,name in enumerate(names,start=start_num):
            # img_link = "https://cryptologos.cc{}".format(link.get('href'))
            print("{} - working on {}".format(count,name))
            html_doc_2 = requests.get("https://coinmarketcap.com/currencies/{}/".format(name))
            if html_doc_2.status_code == 200:
               soup2 = BeautifulSoup(html_doc_2.text, 'lxml')
               test = soup2.select_one(".nameHeader").img
               symbol = test['alt']
               try :
                   open(path.join(directory, symbol+'.png'))
                   print("-- This {} Saved before!\n".format(name))
               except:
                  with open(path.join(directory, symbol+'.png'), "wb") as f:
                          new_link = requests.get(test['src'])
                          f.write(new_link.content)
                          print("-- {} Logo Saved --".format(name))
                          time.sleep(0.3)
            else:
                print("---- Breaked {} to url \n".format(name))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(tasks())


# from os import name, path, symlink
# import bs4
# import requests,time,aiohttp,random
# from requests.sessions import Session, session



# names = ["bitcoin"]
# url="https://api.coingecko.com/api/v3/coins/list"
# directory = r'C:\Users\Hamidreza\Desktop\coins'

# resp = requests.get(url).json()
# for coin in resp[360:1000]:
#     if len(coin["name"]) <= 15: 
#     #    print(coin["name"].replace(" ","-"))
#        names.append(coin["name"].replace(" ","-"))
# async def tasks():
#         for name in names:
#             # img_link = "https://cryptologos.cc{}".format(link.get('href'))
#             print("working on {}".format(name))      
#             html_doc_2 = requests.get("https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=false&developer_data=false&sparkline=false".format(name))
#             if html_doc_2.status_code == 200:
#                symbol = html_doc_2.json()["symbol"]
#                try :
#                    open(path.join(directory, symbol+'.png'))
#                    print("this {} Saved".format(name))
#                except:
#                   with open(path.join(directory, symbol+'.png'), "wb") as f:
#                           new_link = requests.get(html_doc_2.json()["image"]["small"])
#                           f.write(new_link.content)
#                           print("-- {} Saved before --".format(name))
#             else:
#                 print("\n Breaked to url + --------- + {}".format(name))

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(tasks())





# ts = time.time()
# result = []

# def get_tasks(session,url):
#     tasks = []
#     tasks.append(session.get(url,ssl=False))
#     return tasks

# async def get_symbol():
#     async with aiohttp.ClientSession() as session:
#          tasks = get_tasks(session,url)
#          responses = await asyncio.gather(*tasks)
#          for res in responses:
#              result.append(await res.json())
#          for value in result[0]:
#             name  = value["name"]
#             symbol  = value["symbol"]
#             html_doc_2 = await session.get("https://coinmarketcap.com/currencies/{}/".format(name))
#             soup2 = BeautifulSoup(html_doc_2.text, 'lxml')
#             test = soup2.select_one(".nameHeader").img
#             symbol,new_link = test['alt'],requests.get(test['src'])
#             print("working on {}".format(name))
#             with open(path.join(directory, symbol+'.png'), "wb") as f:
#                     f.write(new_link.content)
    
#             #  symbol = await i["symbol"] 
#             #  print(symbol)

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(get_symbol())
