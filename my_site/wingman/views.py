from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
route_table = {
    "config": "Config",
    "io": "IO",
    "bgop": "Background Operations",
    "static": "Static Config",
}

def modules_view(request, module):
    try:
        page = f'Welcome to {route_table[module]}'
        return HttpResponse(page)
    except:
        raise Http404("ACTUAL 404 Message : Page not found as requested")

def num_page_view(request, num_page):
    module_list = list(route_table.keys())
    print(f"Module list : {module_list} {module_list[0]}")
    page = module_list[num_page]

    webpage = reverse("modules", args=[page])
    return HttpResponseRedirect(webpage)

def render_view(request):
    return render(request, "wingman/example.html")