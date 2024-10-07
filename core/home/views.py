from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Abhijit Gupta', 'age': 26},
        {'name': 'Rohan Sharma', 'age': 23},
        {'name': 'Vicky Kaushal', 'age': 17},
        {'name': 'Deepanshu Chaurasiya', 'age': 16},
        {'name': 'Sandeep', 'age': 63},
    ]
    vegetable = ['tomato', 'onion', 'potato']  # Example vegetable list
    
    return render(request, "home/index.html", context={'page':'Django class','peoples': peoples, 'vegetable': vegetable})

def about(request):
    context = {'page':'About'}

    return render(request,"home/about.html",context)

def contact(request):
    context = {'page':'Contact'}
    return render(request,"home/contact.html",context)

def success_page(request):
    print("*" * 10)
    context = {'page':'Contact'}

    return HttpResponse("<h1> Hey this is a sucess page </h1> ")