from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow a user edit his own profile"""

    def has_object_permission(self,request,view,obj):
        """Chechk if the user trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """Allow a user update his own profile"""

    def has_object_permission(self,request,view,obj):
        """Chechk the user is trying to update own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id