from django.shortcuts import render
from django.http import HttpResponse
from .models import MVRS_Category
from .models import Cars
from .forms import BookingForm
from .forms import contactForm
# Create your views here.
def calculate():
    x=1
    y=2
    return x
def home(request):
    #return HttpResponse("hello world")
    #x= calculate()
    return render(request,'index.html')
def about(request):
    #return HttpResponse("about page")
    return render(request,'about.html')
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form = BookingForm()
    dict_form={ 
        'form':form
    }
    #return HttpResponse("booking page")
    return render(request,'bookings.html',dict_form)
def cars(request):
    dict_cars={ 
        'cars': Cars.objects.all()
    }
    #return HttpResponse("cars page")
    return render(request,'cars.html',dict_cars)
def contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm2.html')
    form = contactForm()
    dict_form={ 
        'form':form
    }
    #return HttpResponse("contact page")
    return render(request,'contacts.html',dict_form)
def help(request):
    #return HttpResponse("about page")
    return render(request,'help.html')
def category(request):
    dict_cat={ 
        'cat':MVRS_Category.objects.all()
    }
    #return HttpResponse("contact page")
    return render(request,'category.html',dict_cat)





