from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

from demo.models import Blog

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"