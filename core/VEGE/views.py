from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name =recipe_name,
            recipe_description =recipe_description,
        )


        return redirect('/recipe/')
    
    queryset = Recipe.objects.all()

    # search -------
    if request.GET.get('search'):
        # print(request.GET.get('search'))
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    
    # -------------

    context = {'recipe':queryset}
    return render(request,'recipe.html',context)




def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()

        return redirect('/recipe/')

    context = {'recipe':queryset}


    return render(request,'update_recipe.html',context)




def delete_recipe(request,id):
    # print(id)
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    # return HttpResponse("a")
    return redirect('/recipe/')

# login page
def login_page(request):
    return render(request,'login.html')

# register
def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username Already taken")
            return redirect('/register/')


        user = User.objects.create(
            first_name =first_name,
            last_name = last_name,
            username = username,
            # password = password
        )

        # to encript password
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully")
        return redirect('/register/')

    return render(request,'register.html')