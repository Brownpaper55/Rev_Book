from django.db import models
from django.contrib import auth


# Create your models here.
class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(help_text="The publishers website")
    email = models.EmailField(help_text="Email address of the publisher")

    def __str__(self):
        return self.name


class Contributor(models.Model):
    """A contributor to a book. eg. author, co-author"""
    first_names = models.CharField(max_length=20, help_text="The contributors first name")
    last_names = models.CharField(max_length=20, help_text="Last name of contributor")
    email = models.EmailField(help_text="email of the contributor")

    def __str__(self):
        return self.last_names

class Book(models.Model):
    """Books available on the review site"""
    title = models.CharField(max_length=70, help_text="title or name of the book")
    publication_date = models.DateField(verbose_name="The date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributor = models.ManyToManyField(Contributor, through="BookContributor")

    def __str__(self):
        return self.title

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        Author = "Author", "Author"
        Co_Author = "Co_Author", "Co-Author"
        Editor = "Editor", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Role of the contributor in the book", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content =models.TextField(help_text='The review text')
    rating =models.IntegerField(help_text='The rating the reviewer has given')
    date_created = models.DateTimeField(auto_now_add=True, help_text='The date the review was created')
    date_edited = models.DateTimeField(null=True, help_text='The date and time the review was created')
    creator =models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book =models.ForeignKey(Book, on_delete=models.CASCADE, help_text='The book that this review is for.')
