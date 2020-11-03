from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def index(request):
    return render(request,'home/index.html',{})

def dashbord(request):
    return render(request, 'home/dashbord.html', {})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('Holls-auth:index')
    
    def form_valid(self, form):
        view_info = super(SignUp, self).form_valid(form)
        username , password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username=username,password=password)
        if user:
            login(self.request ,user)
        return view_info

