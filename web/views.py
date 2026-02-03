from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is home page")

def services(request):
    return HttpResponse("This is services page")

def product(request):
    return HttpResponse("This is product page")

def contact(request):
    return HttpResponse("This is contact page")

def about(request):
    return HttpResponse("This is about page")