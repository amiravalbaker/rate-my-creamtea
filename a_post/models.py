from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Post Model
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=255)
    image = CloudinaryField('image')  # Cloudinary image storage
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(
            1), MaxValueValidator(5)]  # Rating must be 1-5
    )
    is_approved = models.BooleanField(
        default=False)  # Admin must approve
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  # Display title in admin panel

    class Meta:
        ordering = ['-created_at']  # Show newest posts first

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(
            1), MaxValueValidator(5)]  # Rating must be 1-5
    )
    is_approved = models.BooleanField(
        default=False)  # Admin must approve comments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {
            self.title}"  # Display who commented and title

    class Meta:
        ordering = ['-created_at']  # Show newest comments first
