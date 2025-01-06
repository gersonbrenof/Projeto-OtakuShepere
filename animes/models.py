from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    usuario = models.OneToOneField(User, related_name="usuarios", on_delete=models.CASCADE)
    nomeUsuarios = models.CharField( max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email
    
    
class Perfil(models.Model):
    fotoPerfil = models.ImageField(upload_to='imagem_perfil')
    favortios = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuarios, related_name="perfil", on_delete=models.CASCADE)

class Obras(models.Model):
    TIPO_OBRA_CHOICES = [
        ('anime', 'Anime'),
        ('manga', 'Manga'),
        ('manwar', 'Manwar'),
    ]
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    dataCriacao = models.DateField(auto_now_add=True)
    sinopse = models.TextField()
    anoLancamento = models.CharField(max_length=15)
    avalicaoMedia = models.IntegerField(default=0)
    imagemCapa = models.ImageField(upload_to='imagem_capa')
    tipoObra = models.CharField(max_length=10, choices=TIPO_OBRA_CHOICES)
    def __str__(self):
        return self.titulo 
    
class Anime(Obras):
    numero_episodes = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero_episodes
    
class Manga(Obras):
    numero_volumes = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero_volumes
    
class Manwar(Obras):
    numero_pages = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero_pages
    