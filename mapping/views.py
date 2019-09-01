from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'mapping/home.html'
