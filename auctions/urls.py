from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    path("watchlistchange/<int:listing_id>", views.changewatchlist, name="watchlist_change"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlistremove/<int:listing_id>", views.watchlistremove, name="watchlist_remove"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("addbid/<int:listing_id>", views.add_bid, name="addbid"),
    path("addcomment/<int:listing_id>", views.add_comment, name="addcomment")
]
