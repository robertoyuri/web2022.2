from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    address = models.TextField()
    cpf = models.CharField(max_length=14)
    def __str__(self):
        return self.cpf + ' - ' + self.name