from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from catalog.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    
    books = Book.objects.all().count()
    books_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        "numbooks": books,
        "books_avail": books_avail
    }
    
    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckedOutBooksByUserView(LoginRequiredMixin, ListView):
    # List all book instances, filter based on currently logged in user session
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5  # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)