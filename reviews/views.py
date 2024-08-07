from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review, Contributor, Publisher
from .utils import average_rating
from .forms import SearchForm, PublisherForm, OrderForm, BookMediaForm
from django.contrib import messages
from io import BytesIO
from PIL import Image
from django.core.files.images import ImageFile 
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
# Create your views here.

def index(request):
    return render(request, 'base.html')


def is_staff_user(user):
    return user.is_staff
@user_passes_test(is_staff_user)



def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book, 'book_rating': book_rating,'number_of_reviews': number_of_reviews})
        context = {'book_list': book_list}
    return render(request, 'reviews/books_list.html', context)

def book_detail(request,pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {"book": book,"book_rating": book_rating,"reviews": reviews}
    else:
        context = {"book": book, "book_rating": None, "reviews": None}
    
    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get('viewed_books', [])
        viewed_book = [book.id, book.title]
        if viewed_book in viewed_books:
            viewed_books.pop(viewed_books.index(viewed_book))
        viewed_books.insert(0, viewed_book)
        viewed_books = viewed_books[:max_viewed_books_length]
        request.session['viewed_books'] = viewed_books

    return render(request, 'reviews/book_detail.html', context)

def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(first_names__icontains=search)
            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
            lname_contributors = Contributor.objects.filter(last_names__icontains=search)
            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
    return render(request, "search.html", {"form": form, "search_text": search_text, "books": books})

#@permission_required('edit_publisher')

def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance= publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher was created{}".format(updated_publisher))
            else:
                messages.success(request, "Publisher{} was updated".format(updated_publisher.pk))
            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "reviews/form-example.html",{'method':request.method, 'Form':form})        


@login_required
def book_media(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookMediaForm(request.POST, request.FILES, instance= book)
        if form.is_valid:
            book = form.save(False)
            image_field = form.cleaned_data.get('image_field')
            if image_field:
                image = Image.open(image_field)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format= image_field.image.format)
                image_file = ImageFile(image_data)
                book.image_field.save(image_field.name, image_file)
                book.save()
                messages.success(request,"Book\"{}\"was successfully updated.".format(Book))
                return redirect("book_detail", book.pk)
    else:
        form = BookMediaForm(instance=book)

    return render(request, "reviews/instance-form.html", {"Form":form, "instance":book, "model_type":"Book", "is_file_upload":True})


