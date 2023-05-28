from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
# Create your views here.

def list_view(request):
    
    cars_list = models.CarsModel.objects.all()
    print(f"Cars list {cars_list}")
    data = {
        "cars": cars_list
    }
    return render(request, 'cars/list.html', context=data)

def add_view(request):

    # if request.POST:
    print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.CarsModel.objects.create(brand=brand, year=year)
        print("In if")
        return redirect(reverse('cars:list'))
    else:
        print("In else")
        return render(request, 'cars/add.html')

def delete_view(request):
    print(f'in delete :  {request.POST}')
    if request.POST:
        pk = int(request.POST["pk"])
        try:
            models.CarsModel.objects.get(pk=pk).delete()
            print("In if")
            return redirect(reverse('cars:list'))
        except:
            print("PK not found")
            return render(request, 'cars/delete.html')
    else:
        return render(request, 'cars/delete.html')