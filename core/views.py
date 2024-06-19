from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    return render(request, 'home.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def menu_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'menu_details.html', {'event': event})


def blog_post_list(request):
    blog_posts = BlogPost.objects.filter(is_gallery=False).order_by('-created_at')
    gallery_items = BlogPost.objects.filter(is_gallery=True).order_by('-created_at')
    return render(request, 'blog_post.html', {'blog_posts': blog_posts, 'gallery_items': gallery_items})

def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})