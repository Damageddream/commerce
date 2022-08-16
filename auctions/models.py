from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64, )
    description = models.CharField(max_length=120)
    starting_bid = models.IntegerField()
    image_url = models.URLField(max_length=200)

class Bids(models.Model):
    bid = models.IntegerField()

class Comments(models.Model):
    comment_text = models.CharField(max_length=200)