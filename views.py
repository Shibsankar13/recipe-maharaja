from django.shortcuts import render, redirect
from myapp.models import Contact
from myapp.models import Recipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
@login_required(login_url='LoginPage')
def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def feature(request):
    return render(request, 'feature.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your Time"
    return render(request, 'contact.html',context)

def recipe(request):
    context={}
    if request.method=="POST":
        data = request.POST
       
        rimage = request.FILES.get('recipe_image')
        rname=data.get('recipe_name')
        ringredients=data.get('recipe_ingredients')
        rdescription=data.get('recipe_description')
       

        obj = Recipe(recipe_name=rname, recipe_ingredients=ringredients, recipe_description=rdescription,recipe_image= rimage)
        obj.save()
        context['message']=f"Dear, Thanks for your Time"

        return redirect('recipe.html')
    
    return render(request, 'recipe.html',context)


def blog(request):
    return render(request, 'blog.html')

def view(request):
     event_list=Recipe.objects.all()
     return render(request,'view.html',
            {'event_list':  event_list})
           
     return render(request, 'view.html')

    
def SignupPage(request):
    if request.method=="POST":
        name = request.POST.get("uname")
        email = request.POST.get("uemail")
        password = request.POST.get("upass")
        passwordc = request.POST.get("upassc")

        if password!=passwordc:
            return HttpResponse("Your password and confirm pass not same")
        else:
            my_user=User.objects.create_user(name,email,password)
            my_user.save()
        return redirect('LoginPage.html')
    return render(request, 'SignupPage.html')

def LoginPage(request):
    if request.method=="POST":
        username = request.POST.get("username")
        passu = request.POST.get("passu")
        user=authenticate(request,username=username,password=passu)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'LoginPage.html')

def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(recipe_name__icontains=query) | Q(recipe_ingredients__icontains=query)
        )
        return object_list
    