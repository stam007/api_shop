from django.urls import include, path
from rest_framework import routers

from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *



router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet)
router.register(r'souscategories',SousCategoriesViewSet)
router.register(r'produit',PoduitViewSet)
router.register(r'otherphoto',OtherPhotoViewSet)
router.register(r'livraison',LivraisonViewSet)
router.register(r'users', UserViewSet)
#router.register(r'auth', ObtainAuthToken)


urlpatterns = [
    #url('categories/', CategoriesViewSet.as_view()),
    #path('users/', UserViewSet.as_view()),
    url('', include(router.urls)),
    url('auth/', ObtainAuthToken.as_view())
]


