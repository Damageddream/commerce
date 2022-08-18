from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    title = models.CharField(max_length=64, )
    description = models.TextField(max_length=300)
    starting_bid = models.IntegerField()
    image_url = models.URLField(max_length=200)
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

class Bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid = models.IntegerField()

    def __str__(self):
        return f"{self.bid}"

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_text = models.CharField(max_length=200)
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = "comment_listing")
    def __str__(self):
        return f"{self.comment_text}"
class Watchlist(models.Model):
    watchlist_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_user")