from django.db import models

# Create your models here.

class Pregunta(models.Model):
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	return self.asunto

    def publicado_hoy(self):
	return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = "se pregunto hoy?"

class Respuesta(models.Model):
    Pregunta = models.ForeignKey(Pregunta)
    contenido = models.TextField()
    mejor_respuesta = models.BooleanField("Respuesta preferida", default = False)

    def __str__(self):
    	return self.contenido
