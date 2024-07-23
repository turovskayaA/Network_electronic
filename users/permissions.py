from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """ Проверка прав на администратора """
    def has_permission(self, request, view):
        return request.user.is_staff
