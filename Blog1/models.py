from django.db import models

class Posty(models.Model):
    autor = models.CharField(max_length=30)
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    data_publikacji = models.DateTimeField()
