from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
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