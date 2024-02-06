from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    code = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.title
