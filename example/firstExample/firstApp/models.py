from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField


class Movies(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=250)
    lead_actor = models.CharField(max_length=250)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

