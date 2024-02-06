from django.urls import path
from books.api.views import Booklists, BookDetailslists


urlpatterns = [
    path("books/", Booklists.as_view()),
    path("books/<int:pk>", BookDetailslists.as_view()),
]
