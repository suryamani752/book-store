from django.db import models

# Create your models here.
class Author(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    created = models.DateTimeField('data created')

class Book(models.Model):
    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=50)
    created = models.DateTimeField('data created')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    price  = models.DecimalField(decimal_places=2, max_digits=4, null=True)