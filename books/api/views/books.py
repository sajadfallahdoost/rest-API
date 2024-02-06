from books.api.serializers import BookSerializer, BookDetailsSerializer
from books.models import Book
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.views.generic import ListView


class Booklists(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailslists(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
