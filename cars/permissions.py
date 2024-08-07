from rest_framework import permissions
class CarOwner(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj):
        if request.method == "GET":
            return True
        if request.user == obj.buyer:
            return True
        else:
            False
    