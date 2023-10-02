from django.db import models


# Models for book resources

class Author(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Location(models.Model):
     title = models.CharField(max_length=50)
    
     def __str__(self) -> str:
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Condition(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title

# Model for books

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name="book_author", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="book_location", on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name="book_genre", on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, related_name="book_condition", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title