from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
	nombre = models.CharField(max_length=140)

	def __str__(self):
		return self.nombre


class Vacante(models.Model):
	titulo = models.CharField(max_length=1000)
	empresa = models.ForeignKey(Empresa, related_name='vacantes')
	aplicantes = models.ManyToManyField(User, related_name='vacantes', blank=True, null=True)

	def __str__(self):
		return "Este es el pinche titulo: {}".format(self.titulo)