from django.contrib import admin
from .models import *


# Admin Config for adding multiple images to Models: Menu and BlogPost
class MenuImageInline(admin.TabularInline):
    model = MenuImage
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuImageInline]


class BlogPostImagesInline(admin.TabularInline):
    model = BlogPostImages
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogPostImagesInline]
    list_display = ('title', 'created_at', 'is_gallery')
    list_filter = ('is_gallery', 'event')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Event)
admin.site.register(BlogPost, BlogPostAdmin)
