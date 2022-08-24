from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Listing, Bids, Comments


def index(request):
    list = Listing.objects.all()
    
    return render(request, "auctions/index.html", {
        "listings": list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    category = ["Fashion", "Toys", "Electronics", "Home", "other"]
    if request.method == "POST":
        lisiting = Listing(poster = request.user, 
        title = request.POST["title"], 
        description = request.POST["description"], 
        starting_bid = request.POST["starting_bid"], 
        image_url = request.POST["image"],
        category = request.POST.get("category", "example"),
        )
        lisiting.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/new_listing.html",{
            "categories": category
        })
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    print(listing.winner)
    if listing.winner != None:
        return render(request, "auctions/closed.html", {
            "listing": listing,
        })
    if request.method == "POST":
        if "watchlist" in request.POST:
            print
            if request.user in listing.watchers.all():
                listing.watchers.remove(request.user)
                listing.save()
                print(listing.watchers.all())
                return render(request, "auctions/listing.html", {
                "listing": listing,
                "logged_user": request.user,
                "watchers": listing.watchers.all})
            else:    
                listing.watchers.add(request.user)
                listing.save()
                print(listing.watchers.all())
                return render(request, "auctions/listing.html", {
                "listing": listing,
                "logged_user": request.user,

            })
        elif "starting_bid" in request.POST:
            if int(request.POST.get("starting_bid")) < listing.starting_bid:
                   messages.warning(request, f"minimial starting bid is {listing.starting_bid}$")
                   return HttpResponseRedirect(reverse("listing", args=[listing.id]))
            else:
                bid = Bids(bidder= request.user, bid=(int(request.POST.get("starting_bid"))))
                bid.save()
                listing.current_bid.add(bid)
                listing.current_bid_default=bid.bid
                listing.save()
                ordered_bids = listing.current_bid.all().order_by("bid")
                highets = ordered_bids.last()
                print(ordered_bids)
                print(request.POST.get("starting_bid"))
                return HttpResponseRedirect(reverse("listing", args=[listing.id]))
        elif "current_bid" in request.POST:
            if int(request.POST.get("current_bid")) <= listing.current_bid_default:
                   messages.warning(request, f"minimial bid is more than {listing.current_bid_default}$")
                   return HttpResponseRedirect(reverse("listing", args=[listing.id]))
            else:
                bid = Bids(bidder= request.user, bid=(int(request.POST.get("current_bid"))))
                bid.save()
                listing.current_bid.add(bid)
                listing.current_bid_default=bid.bid
                listing.save()
                ordered_bids = listing.current_bid.all().order_by("bid")
                highets = ordered_bids.last()
                (print(ordered_bids, highets.bidder ))
                return HttpResponseRedirect(reverse("listing", args=[listing.id]))
        elif "closed" in request.POST:
            ordered_bids = listing.current_bid.all().order_by("bid")
            highets = ordered_bids.last()
            listing.winner = highets.bidder
            listing.active = False
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=[listing.id]))
        elif "comment_text" in request.POST:
            comment = Comments(commenter = request.user, comment_text=request.POST["comment_text"],)
            comment.save()
            listing.comment.add(comment)
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=[listing.id]))



    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "comments": listing.comment.all()
        })

@login_required
def watchlist(request, user_id):
    w_user = User.objects.get(id=user_id)
    watchlist_items = w_user.watchers.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist_items,
    })

def category(request):
    listing = Listing.objects.all()
    categories = []
    for item in listing:
        if item.category in categories:
            next
        else:
            categories.append(item.category)

    return render(request, "auctions/category.html", {
        "listing": listing,
        "categories": categories,
    })
def category_listing(request, category):
    listing = Listing.objects.all()
    listing_id = []

    for item in listing:
        print(item.active)
        if category in item.category and item.active == True:
            listing_id.append(item)
    print(listing_id)
    return render(request, "auctions/category_listing.html", {
        "listing_id": listing_id,
        "listing": listing
    })
