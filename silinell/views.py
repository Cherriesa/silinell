from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.views import LoginView    
from django.http import HttpResponseRedirect
from django.utils.decorators import classonlymethod
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse



class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    def dispatch(self, request, *args, **kwargs):
      if request.user.is_authenticated:
        return redirect('dashboardhome')
      return super(SignUp, self).dispatch(request, *args, **kwargs)


class login(LoginView):
    form_class = UserLoginForm
    success_url = reverse_lazy('')
    template_name = 'login.html'
    

class dashboardhome(View):
  template_name = "dashboard/dashboard-main.html"
  initial = {'key': 'value'}
  def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
  
  
  def post(self, request, *args, **kwargs):
    
   return render(request, self.template_name)

class IncidentDeleteView(DeleteView):
    model = incident
    success_url= '/dashboard/incident'
    
    
    def get(self, *args, **kwargs):
     return self.post(*args, **kwargs)
 
class IncidentUpdateView(UpdateView):
    model = incident
    template_name = ".html"
     

    


class dashboardAddwebsite(View):
    form_class = Formaddwebsbite
    initial = {'key': 'value'}
    template_name = 'dashboard/add-website.html'
    
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        web_list = incident.objects.all().order_by('id')
        counter = incident.objects.count()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(web_list, 5)
        print(paginator.num_pages)
        try:
           weblist_param = paginator.page(page_num)
        except PageNotAnInteger:
            weblist_param = paginator.page(1)
        except EmptyPage:
            weblist_param = paginator.page(paginator.num_pages)
        
        return render(request, self.template_name, {'form': form,'weblist_param': weblist_param,'counter':counter})
  
    
            
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save();
            # <process form cleaned data>
            return HttpResponseRedirect(self.request.path_info)
        
        return render(request, self.template_name, {'form': form})
      
      
class websiteUpdate(UpdateView): 
    model = incident
    template_name = 'update-website.html'

def search_website(request):
        if request.method == "POST":
            search_str = json.loads(request.body).get('searchtxt')
            print(search_str)
            searcher = incident.objects.filter(website_name__startswith = search_str)| incident.objects.filter(status_webstie__startswith = search_str)|incident.objects.filter(
                status_action__startswith= search_str )| incident.objects.filter(
                url__startswith = search_str )|incident.objects.filter(
                message__startswith = search_str )
            
            data = searcher.values()
            print(data)
            
            return JsonResponse(list(data),safe=False)
            
            
    
    


    