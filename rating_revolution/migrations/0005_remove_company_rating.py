# Generated by Django 5.1 on 2024-08-28 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating_revolution', '0004_remove_review_dislikes_remove_review_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='rating',
        ),
    ]
