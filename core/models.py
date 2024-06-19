from django.db import models


class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images', null=True, blank=True)
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    food_type = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name


class Menu(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    food_vendor = models.CharField(max_length=255, default='Unknown')
    description = models.TextField(help_text="Use HTML tags to format the content")
    images = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    nutritional_info = models.TextField(help_text="Use HTML tags to format the content")

    def __str__(self):
        return f"Menu for {self.event.event_name}"


class MenuImage(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_images')
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return f"Image for {self.menu.event.event_name}"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Use HTML tags to format the content")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_gallery = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BlogPostImages(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_post_images', null=True)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Images for {self.blog_post.title}"