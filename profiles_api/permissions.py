from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow a user edit his own profile"""

    def has_object_permission(self,request,view,obj):
        """Chechk if the user trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id