from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher
# Create your views here.

# Below is the function based view
# def classroom_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThanksView(TemplateView):
    template_name = 'classroom/thanks.html'


class TeacherView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    # template : model_list.html
    context_object_name = "teacher_list"


class TeacherDetailView(DetailView):
    model = Teacher
    # template : model_detail.html


class TeacherUpdateView(UpdateView):
    # Shares model_list.html (shares same view with creation)
    model = Teacher
    # fields = ['last_name']
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView(DeleteView):
    # default template view : model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # Note : this is a URL and not a html page redirection
    # success_url = '/classroom/thanks'
    success_url = reverse_lazy('classroom:thanks')

    # What to do with the form
    # form is the connection to the form used in the contact.html file.
    # When a valid form is ported
    def form_valid(self, form):
        #form.save()
        print(form.cleaned_data)
        return super().form_valid(form)