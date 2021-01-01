"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from silinell import views
from django.contrib.auth import views as auth_views
from django.urls import path, include 
from django.views.generic.base import TemplateView # new
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp.as_view(), name='signup_url'),
    path('login/', views.login.as_view(), name='login'),
    path('dashboard/', views.dashboardhome.as_view(), name='dashboard'),
    path('dashboard/incident', views.dashboardAddwebsite.as_view(), name='incident_url'),
    path('dashboard/incident/delete/<int:pk>', views.IncidentDeleteView.as_view(), name='incident_url_del'),
    path('dashboard/incident/search', csrf_exempt(views.dashboardAddwebsite.as_view()), name='incident_search'),


    
    
    
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
