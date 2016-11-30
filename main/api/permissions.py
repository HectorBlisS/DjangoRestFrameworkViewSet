from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.aplicantes.filter(id=request.user.id).exists()