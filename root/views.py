from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'root/index.html')
# Create your views here.
