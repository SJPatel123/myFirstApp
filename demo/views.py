from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,reverse,get_object_or_404
from django.contrib.auth import authenticate, login as dj_login
from django.urls import reverse

from demo.models import Category
from .forms import AddBlogForm
from .models import Tag
# Create your views here.
def base(request):
    return render(request, "base.html")

def index(request):
    category_display=Category.objeccts.all()
    tag_display=Tag.objeccts.all()
    print(category_display.query)

    context={
        "category_display":category_display,
        "tag_display":tag_display,
    }

    return render(request,"index.html",context)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def postdetails(request):
    return render(request, "post-details.html")

def alltags(request,slug):
    tag=Tag.objects.get(slug=slug)

    context={
        "tag":tag,
    }
    return render(request,"see_all_tag.html",context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                dj_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Invalid account")
    else:
        return render(request, "login.html")

def addblog(request):
    if request.method == "POST":
        form = AddBlogForm(data=request.POSTss)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AddBlogForm()
        
    
        context = {
            'form':form
        }

        return render(request,'addblog.html',context)