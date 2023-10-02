from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register(r'genre', GenreViewSet, basename="genre")
router.register(r"author", AuthorViewSet, basename="author")
router.register(r"location", LocationViewSet, basename="location")



urlpatterns = [
    path('', include(router.urls)), 
]
