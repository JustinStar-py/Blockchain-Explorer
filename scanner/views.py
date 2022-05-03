from .mixins import CHNetwork, Redirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import  Query
import time,requests
from .utils import get_tron_balance
from django.template import RequestContext


def handler404(request,exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def home(request):
  response = requests.get("https://api.pancakeswap.info/api/v2/tokens/0xeb35acbd23cf9d1c13d276815b9969effc5c878f").json()['data']['price']
  return render(request,"home.html",{"response":response})



class scanner(Redirect,CHNetwork,ListView):
    template_name = "detail_address_token.html"
    query = []
    network = "ethereum" #deafult
    headers = {'X-API-KEY': 'BQYTMdjncNjDJ2MoWuu1NpHG6SGtnd1f'}
    # def get_queryset(self):
    #     self.query
    #     return self.query
    def get_queryset(self):
        global headers,search
        search = self.kwargs.get("search")
        headers = self.headers ; queryset =  self.query
        return queryset


    def get_context_data(self, *args, **kwargs):
        n = time.time()
        # url = "https://api.bscscan.com/api?module=account&action=txlist&address=%s&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=8KVAI7FBADXY11Z9YR1KQGCGU5Z7PEGG4B"%search
        context = super().get_context_data(*args, **kwargs)
        eth_networks = ["matic","ethereum"]
        if self.network == "ethereum":
        #   for network in eth_networks:
        #     query = Query.objects.network("ethereum")%(network,search)
        #     context[network] =  requests.post('https://graphql.bitquery.io/',json={'query': query}, headers=headers).json()
            query = Query.objects.network("eth_t")%("bsc",search,search)
            context['transaction'] = requests.post('https://graphql.bitquery.io/',json={'query': query}, headers=headers).json()["data"]["ethereum"]
        elif self.network == "tron":
              get_tron_balance(search)
              context['balance'] = list(get_tron_balance(search))
        return context

