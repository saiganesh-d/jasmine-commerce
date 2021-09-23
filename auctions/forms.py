from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Category, Bid, Comment, Listing

# Model form for a new listing
class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image', 'category']
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.Textarea(attrs={'rows':2, 'maxlength': 1000, 'class': 'form-control'}),
                    'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
                    'image': forms.ImageField(),
                    'category': forms.Select(attrs={'class': 'form-control'})
                   
                    }
        labels = {
            'image': 'Image URL'
        }

# Model form for a new bid on a listing
class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets= {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }

# Model form for a new comment on a listing
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': ''
        }
        widgets = {"comment": forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '5000'})}

