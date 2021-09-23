from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Max

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    # Orders category names alphabetically
    class Meta:
        ordering = ['name']

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    created_at = models.DateTimeField(auto_now_add=True)
    watched_by = models.ManyToManyField(User, blank=True, related_name="watchlist")
    
    def __str__(self):
        return f"{self.title}"
    
    def no_of_bids(self):
        """Returns total number of bids on the listing"""
        return self.bids.all().count()
    
    def current_price(self):
        """Works out the current highest bid or if no bids, the starting price"""
        if self.no_of_bids() > 0:
            return round(self.bids.aggregate(Max('amount'))['amount__max'],2)
        else: 
            return self.starting_bid

    def current_winner(self):
        """Tells us who is currently winning the listing"""
        if self.no_of_bids() > 0: 
            return self.bids.get(amount=self.current_price()).user
        else: 
            return None
        
    def is_in_watchlist(self, user):
        """Tells us if it's in the watchlist"""
        return user.watchlist.filter(pk=self.pk).exists()

    class Meta: 
        # Orders listings by most recent first, by default
        ordering = ['-created_at']


class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.amount)

class Comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=5000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)

    class Meta: 
        # Orders comment by most recent first, by default
        ordering = ['-time']

