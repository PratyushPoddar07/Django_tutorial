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
#     vegetable = ['tomato', 'onion', 'potato']  # Example vegetable list
    
    return render(request, "home/index.html", context={'peoples': peoples})

def about(request):
    # context = {'page':'About'}

    return render(request,"home/about.html")

def contact(request):
    # context = {'page':'Contact'}
    return render(request,"home/contact.html")

# def success_page(request):
#     print("*" * 10)
#     context = {'page':'Contact'}

    # return HttpResponse("<h1>Hey I am a Django server</h1> ")

    # return render(request, "home/index.html")
def success_page(request):
    return HttpResponse("<h1>Hey this a success page </h1>")