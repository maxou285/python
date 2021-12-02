from django.db import models
from django.db.models.fields import BooleanField


class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingrédients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = BooleanField(default=False)

    def __str__(self):
        return self.nom, self.prix