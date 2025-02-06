from django.shortcuts import render
from django.shortcuts import HttpResponse
from  django.views.generic import View, TemplateView, FormView, CreateView, ListView
from .forms import UsuarioRegistrarForms, UsuarioEntrarForm
from .models import Obras, Anime, User, Usuarios, Perfil
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import  redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
        context['listanime'] = Obras.objects.filter (Q(tipoObra__icontains = 'manwar'))
        return context

class MangaView(TemplateView):
    template_name = "manga.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listanime'] = Obras.objects.filter (Q(tipoObra__icontains = 'manga'))
        return context
        
class PesquisaView(TemplateView):
    template_name = "pesquisar.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Obras.objects.filter(Q(titulo__contains=kw) | Q(genero__contains=kw) | Q(tipoObra__contains=kw))
        context["results"] = results
        return context
    

class CadastrarView(CreateView):
    template_name = 'cadastrar.html'
    form_class = UsuarioRegistrarForms
    success_url = reverse_lazy("home")  # Altere para a URL correta após o cadastro

    def form_valid(self, form):
        # Pega os dados do formulário
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        nomeUsuarios = form.cleaned_data.get("nomeUsuarios")

        # Cria o usuário com os dados fornecidos
        user = User.objects.create_user(username=email, email=email, password=password)

        # Associando o usuário ao modelo Usuarios
        usuario = form.save(commit=False)  # Não salva automaticamente ainda
        usuario.usuario = user  # Associando o objeto User ao campo 'usuario' de Usuarios
        usuario.save()  # Agora salva o modelo Usuarios com a associação

        # Realiza o login automaticamente
        login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        # Verifica se há uma URL "next" no GET e redireciona para ela, senão vai para 'home'
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return self.success_url
class LoginView(FormView):
    template_name = "login.html"
    form_class = UsuarioEntrarForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        unome = form.cleaned_data.get("email")
        pword = form.cleaned_data.get("password")
        user = authenticate(username=unome, password=pword)
        
        if user is not None and Usuarios.objects.filter(usuario=user).exists():
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Senha e usuario Invalido. Tente Novamente!"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        
@login_required
def perfil_view(request):
    usuario = request.user.usuarios
    perfil = usuario.perfil # para acessa o perfil recionado
    return render(request, 'perfil.html', {'usuario': usuario, 'perfil': perfil})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')