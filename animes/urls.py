from django.urls import path
from .views import HomeView, AnimeView, PesquisaView, MangaView, ManwarView, CadastrarView, LoginView, perfil_view, LogoutView

urlpatterns = [
    path('',  HomeView.as_view(), name='home'),  # Rota básica para testar
    path('anime/', AnimeView.as_view(), name='anime'),  # Rota para visualizar um anime específico
     path('pesquisa/', PesquisaView.as_view(), name='pesquisar'),
     path('manga/', MangaView.as_view(), name='manga'),
     path('manwar/', ManwarView.as_view(), name='manwar'),  # Rota para visualizar um manhwa específico
     path('cadastrar/', CadastrarView.as_view(), name='cadastrar'),  # Rota para cadastrar um novo anime ou manga
     path('login/', LoginView.as_view(), name='login'),  # Rota para fazer login na plataforma  # Rota para fazer logout na plataforma
     path('perfil/', perfil_view, name='perfil'), # Rota para perfil
     path('logout/', LogoutView.as_view(), name='logout'), # Rota para
     # Rota para fazer logout na plataforma  # Rota para fazer logout na plataforma  # Rota para fazer logout na plataforma  # Rota para fazer logout na plataforma  # Rota para fazer logout na plataforma  # Rota para fazer logout
]
