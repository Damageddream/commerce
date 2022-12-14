from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("category", views.category, name="category"),
    path("category/<str:category>", views.category_listing, name="category_listing"),
]
