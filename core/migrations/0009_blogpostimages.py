# Generated by Django 5.0.6 on 2024-06-17 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blogpost_is_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('blog_posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts_images', to='core.blogpost')),
            ],
        ),
    ]