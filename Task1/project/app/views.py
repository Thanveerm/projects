from django.shortcuts import render,redirect




def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def platform(request):
    return render(request,'platform.html')

def work(request):
    return render(request,'work.html')

def company(request):
    return render(request,'company.html')

def contact(request):
    return render(request,'cont.html')

def services(request):
    return render(request,'services.html')







