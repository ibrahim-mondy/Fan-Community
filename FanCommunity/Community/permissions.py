from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    
    # Everyone is allowed
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return bool(user and user.is_authenticated and getattr(user, "role", "") == "Admin")


class IsOwnerOrAdmin(BasePermission):
    
    # Editing/deleting is allowed for the item owner or admin.
    def has_object_permission(self, request, view, obj):
        
        # Reading is allowed for everyone
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not (user and user.is_authenticated):
            return False

        #Admin is always allowed
        if getattr(user, "role", "") == "Admin":
            return True

        # Try to identify the owner
        owner = getattr(obj, "user", None)
        return owner == user
