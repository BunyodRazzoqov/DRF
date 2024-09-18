from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Book


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


class BookList_2(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = []
        for book in Book.objects.all():
            data.append({book.title: book.author})

        return Response(data, status=status.HTTP_200_OK)
