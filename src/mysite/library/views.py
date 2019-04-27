from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author

def hello(request):
    return HttpResponse("Hello Django")


def index(request):
    return render(request, "index.html")


def author_list(request):
    authors = Author.objects.all()
    retval = {'items': authors}
    return render(request, "author_list.html", retval)


def author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    retval = {'item': author}
    return render(request, "author_view.html", retval)

# Create your views here.
