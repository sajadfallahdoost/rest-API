from django.test import TestCase
from books.models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title="my title", author="author", code=1234)

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEqual(expected_object_name, "my title")

    def test_author_content(self):
        book = Book.objects.get(id=1)
        expected_author_name = book.author
        self.assertEqual(expected_author_name, "author")

    def test_code_content(self):
        book = Book.objects.get(id=1)
        expected_code = book.code
        self.assertEqual(expected_code, 1234)
