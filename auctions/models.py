from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.bid}"

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_text = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.comment_text}"

class Listing(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    title = models.CharField(max_length=64, )
    description = models.TextField(max_length=300)
    starting_bid = models.IntegerField()
    current_bid = models.ManyToManyField(Bids, default=0, related_name="current_bid")
    current_bid_default = models.IntegerField(default=0)
    image_url = models.URLField(max_length=200)
    category = models.CharField(max_length=64)
    watchers = models.ManyToManyField(User, blank=True, related_name="watchers")
    winner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="winner", blank=True, null=True)
    comment = models.ManyToManyField(Comments, blank=True, related_name="comment")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"



class Watchlist(models.Model):
    watchlister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlister")
    watchlist= models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist")

    