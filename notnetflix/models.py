from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    orden = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=1024, null=True)

    def __str__(self) -> str:
        return f'{self.orden} - {self.titulo}'
    
class Serie(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    orden = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=1024, null=True)

    def __str__(self) -> str:
        return f'{self.orden} - {self.titulo}'
    
class Anime(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    orden = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=1024, null=True)

    def __str__(self) -> str:
        return f'{self.orden} - {self.titulo}'

