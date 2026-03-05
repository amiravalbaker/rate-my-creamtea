from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category',
                  'price', 'location', 'image', 'rating']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'star-rating-input'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description', 'rating']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'star-rating-input'}),
        }
