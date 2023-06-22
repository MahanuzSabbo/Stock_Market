from django.db import models


# Create your models here.
class customer(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=60,null=True)
  password=models.CharField(max_length=12,null=True)
    

  def __str__(self):
    return self.name
class StockAdmin(models.Model):
    trade_code = models.CharField(max_length=200,null=True,blank=True)
    high = models.CharField(max_length=200,null=True,blank=True)
    low = models.CharField(max_length=200,null=True,blank=True)
    open = models.CharField(max_length=200,null=True,blank=True)
    close = models.CharField(max_length=200,null=True,blank=True)
    volume = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)