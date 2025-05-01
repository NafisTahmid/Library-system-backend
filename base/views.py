from django.shortcuts import render
from .books import books
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def get_books(request):
    return Response(books)

@api_view(["GET"])
def get_book(request, id):
    new_book = None
    for book in books:
        if book["_id"] == id:
            new_book = book
            break
    return Response(new_book)