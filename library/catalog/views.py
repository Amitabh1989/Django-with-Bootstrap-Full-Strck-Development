from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from catalog.models import *
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    
    books = Book.objects.all().count()
    books_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        "numbooks": books,
        "books_avail": books_avail
    }
    
    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('catalog:book_list')


class BookList(ListView):
    # will look for model_form.html
    model = Book
    queryset = Book.objects.order_by('title')
    context_object_name = 'book_list'


class BookDetail(DetailView):
    # will look for model_form.html
    model = Book


class BookUpdate(UpdateView):
    # will look for model_form.html
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('catalog:book_detail')


class BookDelete(DeleteView):
    # will look for model_form.html
    model = Book
    success_url = reverse_lazy('catalog:book_list')