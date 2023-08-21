from django.contrib import admin
from reviews.models import Publisher, Book, BookContributor, Contributor, Review

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)

