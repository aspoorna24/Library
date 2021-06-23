from django.db import models

# Create your models here.
class Librarians(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=12)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
class Sregistr(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=150)
    usn = models.CharField(max_length=15)
    password = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_id = models.CharField(unique=True,max_length=20)
    author = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.book_name

class Issu(models.Model):
    book_name = models.CharField(max_length=200)
    book_id = models.CharField(unique=True,max_length=20)
    usn = models.CharField(max_length=15)
    date = models.DateField()
    
    def __str__(self):
        return self.book_name
