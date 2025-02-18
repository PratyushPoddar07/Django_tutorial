from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# pagination
from django.core.paginator import Paginator


@login_required(login_url="/login/")
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

# logout
def logout_page(request):
    logout(request)
    return redirect('/login/')



# login page
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')

        else:
            login(request,user)
            return redirect('/recipe/')

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

# lecture 19
from django.db.models import Q

def get_students(request):

    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_id__student_id__icontains = search) |
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) |
            Q(student_address__icontains = search)
        )

    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'report/student.html',{'queryset':page_obj})


def see_marks(request,student_id):
    queryset = StudentMarks.objects.filter(student__student_id__student_id = student_id)
    return render(request,'report/see_marks.html',{'queryset':queryset})
