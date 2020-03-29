from django.shortcuts import render
from django.views.generic.base import TemplateView

def index(req):
    return render(req, 'portfolio/home.html')