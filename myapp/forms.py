from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from myapp.models import Questions

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model=User
        fields=[
                "first_name",
                "last_name",
                "username",
                "email",
                "password1",
                "password2",
               ]
        widgets={
                  "first_name":forms.TextInput(attrs={"class":"form-control"}),
                  "last_name":forms.TextInput(attrs={"class":"form-control"}),
                  "username":forms.TextInput(attrs={"class":"form-control"}),
                  "email":forms.TextInput(attrs={"class":"form-control"}),
                }
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=[
            "question",
            "image",
              ]
        widgets={
            "question":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
              }
        labels={
            "question":"QUESTION",
            "image":"IMAGE",
        }
