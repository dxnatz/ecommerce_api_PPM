from rest_framework import permissions

class IsResponsabileProdotti(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Responsabile Prodotti').exists()