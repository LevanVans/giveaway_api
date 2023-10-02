from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import filters




# Filters for resources 

class GenreViewSet(viewsets.ModelViewSet):
    
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre__title']
    
    def list(self, request, *args, **kwargs):
        
           
        
                
        queryset = self.filter_queryset(self.get_queryset())
     
        serialized_data = [{'title': Book.title, "author":Book.author.title,  "genre" : Book.genre.title, "location":Book.location.title, "condition":Book.condition.title  } for Book in queryset]
        
        
        return Response([Book.objects.values("genre__title").distinct()] + serialized_data)  
        
  
  
class AuthorViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__title']
 
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Book.title, "author":Book.author.title,  "genre" : Book.genre.title, "location":Book.location.title, "condition":Book.condition.title  } for Book in queryset]

        return Response([Book.objects.values("author__title").distinct()] + serialized_data)  
    
  
  
    
class LocationViewSet(viewsets.ModelViewSet):

        
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['location__title']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Serialize each book instance into a dictionary with only the fields you want
        serialized_data = [{'title': Book.title, "author":Book.author.title,  "genre" : Book.genre.title, "location":Book.location.title, "condition":Book.condition.title  } for Book in queryset]

        return Response([Book.objects.values("location__title").distinct()] + serialized_data)     


   
    














  
    

