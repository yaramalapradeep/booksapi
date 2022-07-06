from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def booklist(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def book_detail(request, id):
    if request.method == 'GET':
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        book = Book.objects.get(pk=id)
        book.delete()
        return Response("object  deleted successfully")










