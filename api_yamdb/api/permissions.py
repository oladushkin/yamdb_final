from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_authenticated
                and request.user.role == self.ADMIN)


class IsAuthenticated(permissions.BasePermission):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (obj.author == request.user
                    or (request.user.is_authenticated
                        and (request.user.is_superuser
                             or request.user.role == self.ADMIN
                             or request.user.role == self.MODERATOR))
                    )
                )
