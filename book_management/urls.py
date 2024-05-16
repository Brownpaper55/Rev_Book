from django.urls import path
from .views import BookRecordFormView, FormSuccesView, BookCreateView, BookUpdateView

urlpatterns = [
    path('new_book_record',BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccesView.as_view(), name='form_success'),
    path('book_record_create', BookCreateView.as_view(), name ='book_create'),
    path('book_record_update/<int:pk>', BookUpdateView.as_view(), name = 'book_update')
]