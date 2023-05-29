from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm
# Create your views here.

# Below is the function based view
# def classroom_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThanksView(TemplateView):
    template_name = 'classroom/thanks.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'