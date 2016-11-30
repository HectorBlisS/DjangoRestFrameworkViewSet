# from rest_framework import generics
from ..models import Empresa, Vacante
from .serializers import VacanteSerializer, EmpresaSerializer

from rest_framework import viewsets

#Agregamos el login y permisos
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
#PErmisos
from rest_framework.permissions import IsAuthenticated

# decorador para ampliar la claset 
from rest_framework.decorators import detail_route
# importar response:
from rest_framework.response import Response
# mi permiso personalizado
from .permissions import IsEnrolled

class VacantesViewSet(viewsets.ModelViewSet):
	queryset = Vacante.objects.all()
	serializer_class = VacanteSerializer

	authentication_classes = (BasicAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	@detail_route(methods=['post'],
		authentication_classes=[BasicAuthentication],
		permission_classes=[IsAuthenticated])
	def enroll(self, request, *args, **kwargs):
		vacante = self.get_object()
		vacante.aplicantes.add(request.user)
		return Response({'Aplicante agregado':True})

	@detail_route(methods=['get'],
		serializer_class=VacanteSerializer,
		authentication_classes=[BasicAuthentication],
		permission_classes=[IsAuthenticated,IsEnrolled])
	def aplicantes(self, request, *args, **kwargs):
		return self.retrieve(request,*args,**kwargs)


