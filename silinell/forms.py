from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea
from django.utils.safestring import mark_safe

class DateInput(forms.DateInput):
    input_type = 'date'

class Formaddwebsbite(forms.ModelForm):
    class Meta:
        model = incident
        fields = '__all__'
        widget = {
         
        }
class FormComponentGroup(forms.ModelForm):
    class Meta:
        model = component_group
        fields = '__all__'
        widget = {
         
        }
        
class FormComponent(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=component_group.objects.all(),required=False)
    when = forms.DateField(widget=forms.TextInput(     
    attrs={'type': 'date'})
      )  
    class Meta:
        model = component
        fields = '__all__'
        widget = {
             'when':DateInput(),
         
        }
        
class Formaddscheduler(forms.ModelForm):
    when = forms.DateField(widget=forms.TextInput(     
    attrs={'type': 'date'})
      ) 
    message = forms.CharField(max_length=400, required=False)
    class Meta:
        model = schedule_maintance
        fields = '__all__'
        widget = {
            'when':DateInput(),
            'message': Textarea(attrs={'rows':80, 'cols':20}),
           


           
            
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