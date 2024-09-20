from django.urls import path
from book.views import BookList, BookCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('books/all/', BookList.as_view(), name='books'),
    path('books/create/', BookCreateAPIView.as_view(), name='create_book'),
    path('books/detail/<int:pk>/', BookDetailAPIView.as_view(), name='book_create')
]
