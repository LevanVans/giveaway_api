from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register(r'genre', GenreViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"location", LocationViewSet)



urlpatterns = [
    path('', include(router.urls)), 
]
