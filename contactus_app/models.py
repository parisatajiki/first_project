from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=100)
    eitaa = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    instagram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f" {self.title} and name : {self.name}"
