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
        # return HttpResponseRedirect(request, "404.html")

def num_page_view(request, num_page):
    module_list = list(route_table.keys())
    print(f"Module list : {module_list} {module_list[0]}")
    page = module_list[num_page]

    webpage = reverse("modules", args=[page])
    return HttpResponseRedirect(webpage)

def render_view(request):
    return render(request, "shadow/example.html")

def render_variable_view(request):
    data = {
        "first_name": "Amitabh",
        "last_name": "Suman",
        "age": 31,
        "list_of_items": [1, 2, 3],
        "dict_of_task": {"1": "Learn", "2": "Practice", "3": "Implement", "logged_in": True}
    }
    return render(request, "shadow/variable.html", context=data)