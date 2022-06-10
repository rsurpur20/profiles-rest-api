from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ allow users to edit their own profile and not others"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #http.get
            return True
         #http.delete, http.put, http.patch to only ur user
        return obj.id == request.user.id
        
            