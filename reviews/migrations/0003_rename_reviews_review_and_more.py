# Generated by Django 4.2 on 2023-06-25 19:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_book_contributor_reviews_bookcontributor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Contributor',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='first_name',
            new_name='first_names',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='last_name',
            new_name='last_names',
        ),
    ]
