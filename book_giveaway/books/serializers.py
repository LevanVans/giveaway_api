from rest_framework import serializers

from .models import *



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        

class LocationSerializer (serializers.Serializer):
    class Meta:
        model = Location
        fields = "__all__"
    
    
class GenreSerializer (serializers.Serializer):
    class Meta:
        model = Genre
        fields = "__all__"    


class ConditionSerializer (serializers.Serializer):
    class Meta:
        model = Condition
        fields = "__all__"

        
class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = "__all__"