from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categories,SousCategories,Produit,OtherPhoto,Livraison
# Register your models here.
admin.site.register(Categories)
admin.site.register(SousCategories)
admin.site.register(Produit)
admin.site.register(OtherPhoto)
admin.site.register(Livraison)




