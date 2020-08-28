# Generated by Django 3.0.6 on 2020-06-17 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0008_apartments_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='favorits',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]