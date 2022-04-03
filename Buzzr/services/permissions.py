from rest_framework.permissions import BasePermission


class SuperUserPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role == "SU"
        )


class MerchantPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role == "MM"
        )


class GroupManagerPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role == "GM"
        )


class CustomerPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role == "CU"
        )
