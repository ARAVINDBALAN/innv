from django.shortcuts import render,redirect,get_object_or_404
from bs4 import BeautifulSoup as bf 
from requests import get
from .forms import *
from .models import *
from django.contrib.auth import login
from django.views.generic import FormView
# Create your views here.


def scarp():
    page = get('https://ndma.gov.in/en/alerts.html',verify=False)
    soup = bf(page.text,'html.parser')
    f = soup.find('ul',class_='latestnews')
    f=f.text
    o = f.find('FOR FURTHER')
    return f[:o]


def notify(request):
    st = scarp()
    return render(request,'disaster/index.html',{'notification':st})




def help_page(request):
    if request.method == 'POST':
        form = Help_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Help_form()
    return render(request,'disaster/help.html',{'form':form})                

class HelpView(FormView):
    model = Help
    form_class = Help_form
    template_name = 'disaster/help.html'

from django.views.generic import TemplateView,DetailView,CreateView
from .models import DisasterDetails
# Create your views here.


# class SignUp(CreateView):
#     form_class =
#     success_url=reverse_lazy('login')
#     template_name='disaster/signup.html'
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(phone=phone, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'disaster/signup.html', {'form': form})  



def home(request):
    list = DisasterDetails.objects.all()
    return render(request,'disaster/home.html',{'list':list})

class DisasterDetailsView(DetailView):
    context_object_name = 'detail_list'
    model = DisasterDetails
    template_name='disaster/disaster_detail.html'
