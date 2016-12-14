from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, studentalumniinfo):
        if request.user:
            return studentalumniinfo.user == request.user
        return False
