from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    phone = models.CharField(max_length=14)
    active = models.BooleanField(max_length=100)

    def __str__(self):
        return self.name
