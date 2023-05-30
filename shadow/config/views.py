from django.shortcuts import render
from django.urls import reverse_lazy
from config.models import *
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
import json
from django.http import HttpResponse
# Create your views here.

class ConfigView(CreateView):
    model = Configuration
    fields = '__all__'
    success_url = reverse_lazy('config:step_list')


class StepList(ListView):
    model = Configuration
    queryset = Configuration.objects.order_by('id')
    context_object_name = 'step_list'


class StepDetails(DetailView):
    model = Configuration


class StepsDownloadView(ListView):
    model = Configuration

    # def render_to_response(self, context, **response_kwargs):
    def get(self, request, *args, **kwargs):
        # Get the list of submitted steps
        submitted_steps = list(self.get_queryset().values())

        # Convert the list to JSON
        json_data = json.dumps(submitted_steps, indent=4)

        # Create the HTTP response with the JSON data
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="submitted_steps.json"'

        return response