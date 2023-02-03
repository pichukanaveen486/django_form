from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse



def django_form(request):
    formobject=StudentForm()
    d={'form':formobject}

    if request.method=='POST':
        Fd=StudentForm(request.POST)
        if Fd.is_valid():
            n=Fd.cleaned_data['name']
            a=Fd.cleaned_data['age']
            e=Fd.cleaned_data['email']
            g=Fd.cleaned_data['gender']
            d1={'n':n,'a':a,'e':e,'g':g}
            return render(request,'form_data.html',d1)




    return render(request,'django_form.html',d)
