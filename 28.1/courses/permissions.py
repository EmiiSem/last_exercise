from rest_framework import permissions

class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Модераторы').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Дополнительная логика для проверки прав доступа к объекту
        return False