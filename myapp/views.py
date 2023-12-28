from django.shortcuts import render, redirect,get_object_or_404
from .models import usermodel
from .models import house


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        usermodel.objects.create(email=email, password=password)
        return redirect('login')
    return render(request, "signup.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if usermodel.objects.filter(email=email, password=password).exists():
            return redirect('index')
    return render(request, "login.html")


def housedetails(request):
    if request.method == 'POST':
        housename = request.POST['housename']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        cost = request.POST['cost']
        house.objects.create(housename=housename,phonenumber=phonenumber,address=address,cost=cost)
        return redirect('index')

    return render(request, "housedetails.html")

def house_details(request, house_id):
  houses = get_object_or_404(house, pk=house_id)
  return render(request, 'house_details.html', {'houses': houses})