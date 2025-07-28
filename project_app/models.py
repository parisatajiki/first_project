from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    adress = models.CharField(max_length=150)

    def __str__(self):
        return self.name
