# Generated by Django 5.0.6 on 2024-06-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='food_vendor',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
