from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .Serializers import *
from .models import Categories,SousCategories,Produit,OtherPhoto,Livraison
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        categories=Categories.objects.all()
        serializer_class = CategoriesSerializer(categories, many=True)
        return Response(serializer_class.data)

class SousCategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SousCategories.objects.all()
    serializer_class = SousCategoriesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        souscategories=SousCategories.objects.all()
        serializer_class = SousCategoriesSerializer(souscategories, many=True)
        return Response(serializer_class.data)


class PoduitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        produit=Produit.objects.all()
        serializer_class = ProduitSerializer(produit, many=True)
        return Response(serializer_class.data)



class OtherPhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OtherPhoto.objects.all()
    serializer_class = OtherPhotoSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        otherphoto=OtherPhoto.objects.all()
        serializer_class = OtherPhotoSerializer(otherphoto, many=True)
        return Response(serializer_class.data)


class LivraisonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        livraison=Livraison.objects.all()
        serializer_class = LivraisonSerializer(livraison, many=True)
        return Response(serializer_class.data)