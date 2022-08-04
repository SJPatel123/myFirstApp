from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("base/",views.base,name="base"),
    path("index/",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("postdetails/",views.postdetails,name="postdetails"),
    path("login/",views.login,name="login"),
    path("addblog/",views.addblog,name="addblog"),
    path('<slug:slug>/alltags',views.alltags,name="alltags")
]