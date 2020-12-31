from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class Formaddwebsbite(forms.ModelForm):
    
    class Meta:
        model = incident
        fields = '__all__'
        widget = {
            
        }

    
class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password','id': 'inputPassword','placeholder':'Password'}),
    label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password','id': 'inputPassword2','placeholder':'Password'}),
    label='')
    class Meta:
        model = CustomUser
        fields = ('name', 'email' , 'username','password1','password2' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id': 'inputName','placeholder':'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id': 'inputEmail','placeholder':'email'}),
            'username': forms.TextInput(attrs={'class': 'form-control','id': 'inputUsername','placeholder':'username'}),
           
            
         }
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))        
        
        

        
    


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    list_display = ('name', 'email', 'username')
    list_filter = ('username',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email',  'password1', 'password2', ),
        }),
    )


# Re-register UserAdmin
admin.site.register(CustomUser, UserAdmin)