from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Usuarios(models.Model):
    usuario = models.OneToOneField(User, related_name="usuarios", on_delete=models.CASCADE)
    nomeUsuarios = models.CharField( max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Garantir que o username do User seja igual ao email
        self.usuario.username = self.email
        self.usuario.save()
        super().save(*args, **kwargs)
    
class Perfil(models.Model):
    fotoPerfil = models.ImageField(upload_to='imagem_perfil')
    favortios = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuarios, related_name="perfil", on_delete=models.CASCADE)
    # Sinal para criar o perfil automaticamente
@receiver(post_save, sender=Usuarios)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    
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
    avaliacao = models.IntegerField(default=0)
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
    