from django.contrib import admin

# Register your models here.

from .models import Author, Book, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'birth_date']

#dzięki poniższemu kodowi i podpięciu w admin.site.register lsita pól do edycji została ograiczona (nie ma komentarzy)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'publication_date']
    list_display = ['title', 'get_authors', 'publication_date']

    def get_authors(selfself, obj):
        authors = [i.surname for i in obj.author.all()]
        return ", ".join(authors)

    get_authors.short_description = "Authors"

#       authors =[]
#


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
