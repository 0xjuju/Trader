from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=42, default="", unique=True)
    private_key = models.CharField(max_length=66, default="", unique=True)
    chain = models.CharField(max_length=15, default="")
    index = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.name


