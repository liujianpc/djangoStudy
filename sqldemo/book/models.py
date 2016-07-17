from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    
    def __unicode__(self):
        return self.name