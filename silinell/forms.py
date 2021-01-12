from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.utils.safestring import mark_safe

class Formaddwebsbite(forms.ModelForm):
  
    class Meta:
        model = incident
        fields = ('website_name','status_action','status_website','stickied','url','message')
        widget = {


           
            
        }
        
class Formaddscheduler(forms.ModelForm):
  
    class Meta:
        model = schedule_maintance
        fields = ('name','message','when')
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