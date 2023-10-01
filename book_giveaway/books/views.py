from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import filters




# Filters for resources 

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Author.title } for Author in queryset]
        return Response(serialized_data)  
  
  
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = GenreSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
 
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Author.title } for Author in queryset]
        return Response(serialized_data)  
    
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Location.title } for Location in queryset]
        return Response(serialized_data)     


class BookByGenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Genre.title } for Genre in queryset]
        return Response(serialized_data)    
    



















# Filter for books by resources

 
   
class BooksFilterViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Book.title, "author": Book.author.title, "condition":Book.condition.title, "genre":Book.genre.title, "location": Book.location.title } for Book in queryset]
        return Response(serialized_data)    
    

