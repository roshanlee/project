from django.db import models

# Create your models here.
class mymodel(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.name



