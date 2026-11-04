from rest_framework import permissions

class ModeratorPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Moderators').exists():
            return True
        return False


class OwnerPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner