from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Book
from book.serializer import BookSerializer


# Create your views here.

class BookList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = {}
        for book in Book.objects.all():
            data[book.title] = {
                "author": book.author,
                "title": book.title,
                "description": book.description,
                "created_at": book.created_at,
            }
        return Response(data, status=status.HTTP_200_OK)


class BookCreateAPIView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
