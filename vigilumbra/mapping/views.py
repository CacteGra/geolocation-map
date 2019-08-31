from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Point, WorldBorder
from django.views.generic import TemplateView

def world_view(request):
    world = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(world, content_type='json')


class MainPageView(TemplateView):
    template_name = 'mapping/home.html'
