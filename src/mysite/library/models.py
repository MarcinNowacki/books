from django.db import models


class Author(models.Model):
    surname = models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.surname + " " + self.name


class Comment(models.Model):
    email = models.EmailField()
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ManyToManyField(Author)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.title
