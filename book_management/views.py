from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views import View
from .forms import BookForm
from .models import Book
# Create your views here.
class BookRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/book_management/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class FormSuccesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")
    

class BookCreateView(CreateView):
    model = Book
    fields = ['name','author']
    template_name = 'book_form.html'
    success_url = '/bookmanagement/entry_success'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['name','author']
    template_name = 'book_form.html'
    success_url = '/bookmanagement/entry_success'