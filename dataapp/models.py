
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.core.validators import int_list_validator



class Categories(models.Model):
   title = models.CharField(max_length=32)


class SousCategories(models.Model):
    title = models.CharField(max_length=32)
    idc = models.IntegerField()



class Produit(models.Model):
    name = models.CharField(max_length=32)

    idsc = models.IntegerField()
    address = models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    prix = models.IntegerField()




class OtherPhoto(models.Model):

    idp = models.IntegerField()

    address = models.CharField(max_length=200)



class Livraison(models.Model):

    idop = models.IntegerField()

    dataclient = models.TextField(max_length=1000)


    time = models.TextField(max_length=50)
