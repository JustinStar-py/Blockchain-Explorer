from django.db import models
from django.db.models import query

class get_query(models.Manager):
    def network(self,data):
        change_query = self.filter(name=data)
        for i in change_query:
            net =  i.query
        return net

# Create your models here.
class Network(models.Model):
         network = models.CharField(max_length=10,verbose_name="Network")

         def __str__(self):
             return self.network

class Query(models.Model):
         name = models.CharField(max_length=10)
         query = models.TextField(verbose_name="data")

         def __str__(self):
             return self.name

         objects = get_query() 