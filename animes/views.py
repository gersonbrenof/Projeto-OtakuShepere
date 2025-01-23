from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Obras, Anime
from django.db.models import Q

class HomeView(ListView):
    model = Obras
    template_name = 'home.html'
    context_object_name = 'obras'
    
    def get_queryset(self):
        return Obras.objects.all()

class AnimeView(TemplateView):
    template_name = "animes.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listanime'] = Obras.objects.filter (Q(tipoObra__icontains = 'anime'))
        return context
class ManwarView(TemplateView):
    template_name = "manwar.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listamanwar'] = Obras.objects.filter (Q(tipoObra__icontains = 'manwar'))

class MangaView(TemplateView):
    template_name = "manga.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listamanga'] = Obras.objects.filter (Q(tipoObra__icontains = 'manga'))
        
class PesquisaView(TemplateView):
    template_name = "pesquisar.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Obras.objects.filter(Q(titulo__contains=kw) | Q(genero__contains=kw) | Q(tipoObra__contains=kw))
        context["results"] = results
        return context