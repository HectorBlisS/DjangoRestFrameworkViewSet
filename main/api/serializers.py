from rest_framework import serializers
from ..models import Empresa, Vacante
from django.contrib.auth.models import User

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username']

class VacanteSerializer(serializers.ModelSerializer):
	# empresa = EmpresaSerializer(many=True, read_only=True)
	aplicantes = UserSerializer(many=True, read_only=True)
	class Meta:
		model = Vacante