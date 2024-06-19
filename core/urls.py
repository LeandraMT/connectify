from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('menu_details/<int:event_id>/', views.menu_details, name='menu_details'),
    path('blogs/', views.blog_post_list, name='blog_post_list'),
    path('blogs/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
