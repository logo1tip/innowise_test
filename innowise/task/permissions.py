from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSupport(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "SP" and request.user.is_active:
            return True


class IsUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "US" and request.user.is_active:
            return True
