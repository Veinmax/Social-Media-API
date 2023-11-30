from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrIfAuthenticatedReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (obj.owner == request.user)
        )


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS
            or (
                request.method in ("PUT", "PATCH", "DELETE")
                and request.user == obj.owner
            )
        )


class IsOwnerLikedOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or obj.like == request.user)
