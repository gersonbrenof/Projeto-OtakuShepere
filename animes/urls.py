from django.urls import path
from .views import HomeView, AnimeView, PesquisaView, MangaView, ManwarView

urlpatterns = [
    path('',  HomeView.as_view(), name='home'),  # Rota básica para testar
    path('anime/', AnimeView.as_view(), name='anime'),  # Rota para visualizar um anime específico
     path('pesquisa/', PesquisaView.as_view(), name='pesquisar'),
     path('manga/', MangaView.as_view(), name='manga'),
     path('manwar/', ManwarView.as_view(), name='manwar'),  # Rota para visualizar um manhwa específico
]
