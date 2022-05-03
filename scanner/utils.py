from decimal import Decimal
import requests


def get_tron_balance(address):
      url = "https://apilist.tronscan.org/api/account?address={address}".format(address=address)
      index = -1
      values,tokenName,tokenAbbr,tokenDecimal,tokenLogo,tokenId = [],[],[],[],[],[]
      a = []
      response = requests.get(url).json()
      for i in response["tokenBalances"]:
          index += 1
          zeros = "0" * response["tokenBalances"][index]["tokenDecimal"]
          divisionـnumber = int(f"1{zeros}")
          balance_amount = float(response["tokenBalances"][index]["balance"])
          tokenName.append(response["tokenBalances"][index]["tokenName"])
          tokenDecimal.append(response["tokenBalances"][index]["tokenDecimal"])
          tokenAbbr.append(response["tokenBalances"][index]["tokenAbbr"])
          tokenLogo.append(response["tokenBalances"][index]["tokenLogo"])
          tokenId.append(response["tokenBalances"][index]["tokenId"])
          values.append(format(Decimal(balance_amount/divisionـnumber), '.6f'))
      for l in zip(tokenLogo,tokenName,tokenAbbr,values,tokenDecimal,tokenId):
           a.append(l)
      return a



# import requests,aiohttp,asyncio

# address = ["TTXojNiH2hFL3mUC8yTGMwCQ17pmNFxvzE","TRUVJMsYwcGZL5ywSf4dR6A89Br9UwiZLP"]
# headers = {'X-API-KEY': 'BQYTMdjncNjDJ2MoWuu1NpHG6SGtnd1f'}
# data = """
# {
#   tron {
#     in: transfers(receiver: {is: "%s"}) {
#       amount
#       success
#       txHash
#       currency {
#         name
#         symbol
#       }
#       date {
#         date
#       }
#     }
#     out: transfers(sender: {is: "%s"}) {
#       amount
#       success
#       txHash
#       currency {
#         name
#         symbol
#       }
#       date {
#         date
#       }
#     }
#   }
# }
# """%(address[0],address[0])
# url = 'https://graphql.bitquery.io/'


# async def send_request():
#       async with aiohttp.ClientSession() as session:
#            async with  session.post(url,json={'query': data}, headers=headers) as resp:
#                 responses = await resp.json()
#                 print("-----------------------------------\n"+responses)
#                 print(send_request)