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
from django.template import RequestContext
from django.http import JsonResponse
from django.template.loader import render_to_string
import math
from django.contrib.messages.views import SuccessMessageMixin


def handler404(request, *args, **argv):
    response = render(request,'404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request,'500.html')
    response.status_code = 500
    return response

def badgesnotif_processor(request):
  schedule_maintances = schedule_maintance.objects.all().count()
  incidents = incident.objects.all().count()
  return {'incidents': incidents,'schedule_maintances':schedule_maintances}


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
 
class IncidentUpdateView(SuccessMessageMixin,UpdateView):
    model = incident
    template_name = 'dashboard/incident/update-incident.html'
    fields = '__all__'
    success_url ="/dashboard/incident"
    success_message = "%(name)s was update successfully"

     

class IncidentCreateView(SuccessMessageMixin,CreateView):
    template_name="dashboard/incident/add-incident.html"
    model = incident
    fields = '__all__'
    success_url= '/dashboard/incident'
    success_message = "%(name)s was created successfully"


    
    

class dashboardAddwebsite(View):
    form_class = Formaddwebsbite
    initial = {'key': 'value'}
    template_name = 'dashboard/incident/list-incident.html'

    
    
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        web_list = incident.objects.all().order_by('id')
      
        
        
        return render(request, self.template_name, {'form': form,'weblist_param': web_list})
  
    
            
    def post(self, request, *args, **kwargs):
        htmldata = dict()
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save();
            return HttpResponseRedirect(self.request.path_info)
        context  = {'form': form}
        return render(request, self.template_name, context)
    
    
class SchedulerCreateView(CreateView):
    template_name="dashboard/scheduler/add-scheduler.html"
    model = schedule_maintance
    fields = ['name','message','when']
    success_url= '/dashboard/scheduler'


class SchedulerListView(ListView):
    model = schedule_maintance
    template_name="dashboard/scheduler/list-scheduler.html"
    context_object_name = 'schedule_maintance'
    
class SchedulerDeleteView(DeleteView):
    model = schedule_maintance
    success_url= '/dashboard/scheduler'
    def get(self, *args, **kwargs):
     return self.post(*args, **kwargs)
 
class SchedulerUpdateView(UpdateView):
    model = schedule_maintance
    template_name="dashboard/scheduler/update-scheduler.html"
    fields = ['name','message','when']
    success_url= '/dashboard/scheduler'





def search_website(request):
        getalldata = incident.objects.all().order_by('id')
        htmldata = dict()
        if request.method == "POST":
            search_str = json.loads(request.body).get('searchtxt')
            if search_str == "":
                searcher = getalldata
                print("data kosong revert ke all data")
            else:
                searcher = incident.objects.filter(name__icontains= search_str)| incident.objects.filter(status_Downtime__icontains = search_str)|incident.objects.filter(
                status_action__icontains= search_str )| incident.objects.filter(
                message__icontains = search_str )
             
            
        
        
        data = searcher.values()
        weblist_param = data
        
        print(data)
       
       
            
   
        context  = {'weblist_param': weblist_param}
        htmldata['html_data'] = render_to_string('dashboard/incident/list-incident-component.html', context, request=request)
        return JsonResponse(htmldata, safe=False)
            
    
    


    