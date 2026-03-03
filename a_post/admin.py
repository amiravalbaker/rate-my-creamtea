from django.contrib import admin
from .models import Post, Comment

# Register your models here.
from .models import Post, Comment

# Custom Actions for Posts
def approve_posts(modeladmin, request, queryset):
    """Approve selected posts"""
    queryset.update(is_approved=True)

approve_posts.short_description = "Approve selected posts"

def reject_posts(modeladmin, request, queryset):
    """Reject selected posts"""
    queryset.update(is_approved=False)

reject_posts.short_description = "Reject selected posts"

# Custom Actions for Comments
def approve_comments(modeladmin, request, queryset):
    """Approve selected comments"""
    queryset.update(is_approved=True)

approve_comments.short_description = "Approve selected comments"

def reject_comments(modeladmin, request, queryset):
    """Reject selected comments"""
    queryset.update(is_approved=False)

reject_comments.short_description = "Reject selected comments"

# Post Admin Configuration
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'price',
                    'rating', 'is_approved', 'created_at']
    list_filter = ['category', 'is_approved', 'created_at', 'user__username']
    search_fields = ['title', 'description', 'location',
                     'rating', 'user__username']
    actions = [approve_posts, reject_posts]
    fieldsets = (
        ('User & Title', {
            'fields': ('user', 'title')
        }),
        ('Content', {
            'fields': ('description', 'category')
        }),
        ('Details', {
            'fields': ('price', 'location', 'image', 'rating')
        }),
        ('Status', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Hides by default
        }),
    )

    # Make timestamps read-only
    readonly_fields = ['created_at', 'updated_at']

# Comment Admin Configuration
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'post', 'rating',
                    'is_approved', 'created_at']
    list_filter = ['is_approved', 'rating', 'created_at', 'user__username']
    search_fields = ['title', 'description', 'user__username', 'post__title']
    actions = [approve_comments, reject_comments]
    fieldsets = (
        ('Post & User', {
            'fields': ('post', 'user')
        }),
        ('Content', {
            'fields': ('title', 'description', 'rating')
        }),
        ('Status', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Make timestamps read-only
    readonly_fields = ['created_at', 'updated_at']


