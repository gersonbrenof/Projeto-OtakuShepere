from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import Obras

class HomeView(ListView):
    model = Obras
    template_name = 'home.html'
    context_object_name = 'obras'
    
    def get_queryset(self):
        return Obras.objects.all()



