from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    """
    Clase modelo de publicacion
    """

    titulo = models.CharField('Titulo', max_length=200, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=200, blank=False, null=False)
    contenido = RichTextField('Contenido')
    portada = models.URLField('Portada', max_length=255)
    activo = models.BooleanField('Publicacion Activa', default=True)
    creado = models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    modificado = models.DateTimeField('Fecha de ultima modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f'{self.titulo}'