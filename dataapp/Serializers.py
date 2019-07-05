from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categories,SousCategories,Produit,OtherPhoto,Livraison

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Categories
        fields = ('id','title')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
         user=User.objects.create_user(**validated_data)
         return  user




class SousCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategories
        fields = ('id','title','idc')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id','name','idsc','address','description','prix')



class OtherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPhoto
        fields = ('id','idp','address')






class LivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraison
        fields = ('id','idop','dataclient','time')
