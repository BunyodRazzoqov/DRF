from django.urls import path
from book.views import BookList,BookList_2

urlpatterns = [
    path('books/all/', BookList.as_view(), name='books'),
    path('books/al/', BookList_2.as_view(), name='books2')
]
