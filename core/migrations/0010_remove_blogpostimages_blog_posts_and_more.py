# Generated by Django 5.0.6 on 2024-06-17 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_blogpostimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpostimages',
            name='blog_posts',
        ),
        migrations.AddField(
            model_name='blogpostimages',
            name='blog_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_images', to='core.blogpost'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='core.event'),
        ),
    ]