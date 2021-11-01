from django.forms import fields
from .models import BlogModel,UserModel
from django import forms
class Userform(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username','email']


class Blogform(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','date_added','post']
