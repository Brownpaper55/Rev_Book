# Generated by Django 4.2 on 2023-04-16 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title or name of the book', max_length=70)),
                ('publication_date', models.DateField(verbose_name='The date the book was published')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number of the book')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='The contributors first name', max_length=20)),
                ('last_name', models.CharField(help_text='Last name of contributor', max_length=20)),
                ('email', models.EmailField(help_text='email of the contributor', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='The review text')),
                ('rating', models.IntegerField(help_text='The rating the reviewer has given')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The date the review was created')),
                ('date_edited', models.DateTimeField(help_text='The date and time the review was created', null=True)),
                ('book', models.ForeignKey(help_text='The book that this review is for.', on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Author', 'Author'), ('Co_Author', 'Co-Author'), ('Editor', 'Editor')], max_length=20, verbose_name='Role of the contributor in the book')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.contributor')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Contributor',
            field=models.ManyToManyField(through='reviews.BookContributor', to='reviews.contributor'),
        ),
        migrations.AddField(
            model_name='book',
            name='Publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.publisher'),
        ),
    ]