import requests
from .models import Query
from django.http.response import Http404
from django.shortcuts import redirect
import json
import asyncio

class Redirect():
    def dispatch(self,request,*args,**kwargs):
        search_value = self.request.GET.get("search")
        req = str("{}/{}".format(self.request.path,search_value))
        search_slug_address = self.kwargs.get("search")
        # Search is <slug:search> in url.py 
        if not search_slug_address:
            return redirect(req.replace(" ","-"))
        return super().dispatch(request, *args, **kwargs)

def return_query(search,network):
    global obj,base_network
    if "0x" in search:
       obj = Query.objects.network(network)%("bsc",search)  
    else:
       obj = Query.objects.network(network)%(search,search) 
    base_network = network
    return obj
  


class CHNetwork():
    def dispatch(self,request,*args,**kwargs):
         networks = {"ethereum":42,"tron":"T","solana":44,"solana_2":43,"bitcoin":34,"bitcoin_2":"bc","bitcoin3":36}
         search = self.kwargs.get("search")
         url = 'https://graphql.bitquery.io/'

         if len(search) > 13:
            for net in networks.keys():
               if networks["bitcoin_2"] in search[0:2] or len(search) == 36 and not networks["tron"] in search[0:2]:
                  return_query(search,"bitcoin")

               elif len(search) == networks[net] and not networks["tron"] in search[0:2] and not len(search) == 36:
                  return_query(search,f"{net}")

               elif networks["tron"] in search[0]:
                  return_query(search,"tron")
                  
               self.query = requests.post(url,json={'query': obj}, headers=self.headers).json()
               self.network = base_network

         else:
            self.query = requests.get("https://api.coingecko.com/api/v3/coins/{}?localization=false&market_data=true&community_data=true&sparkline=false".format(search.lower())).json()
         return super().dispatch(request, *args, **kwargs)


#         return super().dispatch(request, *args, **kwargs)
        # if network["eth"] in search:
        #   GNFD = dict((v,k) for k,v in network.items()).get(network["eth"])
        #   self.query = Query.objects.network(GNFD)%("bsc",search)  
  
        # elif network["trx"] in search[0]: 
        #   GNFD = dict((v,k) for k,v in network.items()).get(network["trx"])
        #   self.query = Query.objects.network(GNFD)%(search,search)  

        # elif len(search) == 44: 
        #   GNFD = dict((v,k) for k,v in network.items()).get(network["solana"])
        #   self.query = Query.objects.network(GNFD)%(search,search)

        # elif len(search) == 34: 
        #   GNFD = dict((v,k) for k,v in network.items()).get(network["btc"])
        #   self.query = Query.objects.network(GNFD)%(search,search)
 