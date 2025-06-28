from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):
    # Custom permission to only allow moderators to access certain views.
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator