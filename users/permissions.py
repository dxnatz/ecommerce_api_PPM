from rest_framework import permissions

class IsModeratore(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Moderatore').exists()