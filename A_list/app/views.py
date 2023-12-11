from django.shortcuts import render

from .models import Course

def home(request):
    c = Course.objects.all()
    return render(request,'home.html',{'courses':c})

