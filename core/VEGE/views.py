from django.shortcuts import render

# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        print(recipe_description) 
        print(recipe_name) 
        print(recipe_image) 

    return render(request,'recipe.html')