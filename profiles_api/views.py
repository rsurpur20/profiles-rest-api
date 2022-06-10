from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication #gives u a random string that acts like a password
from profiles_api import permissions

from profiles_api import serializers
from profiles_api import models



class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer #whenever u have a post, put or patch, expect the name field

    def get(self,request,format=None):
        """returns a list of api view features"""
        an_apiview = [
            'Uses HTTP Methods as functions (get, post, patch, put delete)',
            'is similar to a traditional django view',
            'gives you the most control ovr your application logic',
            'is mapped manually to urls',
        ]
        #must return a reponse object
        return Response({ 'message': 'Hello',
                        'an_apiview': an_apiview}) #converts list/dictionary to json to response


    def post(self,request):
        """create  a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): #validate a serializer
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({message: message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk= None):
        """handle updating an object with full replacement"""
        return Response({'method':'PUT'})

    def patch(self,request,pk= None):
        """handle a partial updating an object"""
        return Response({'method':'PATCH'})      

    def delete(self,request,pk= None):
        """delete an object in database"""
        return Response({'method':'DELETE'})   

class HelloViewSet(viewsets.ViewSet):
    """tests api viewset"""

    serializer_class  = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses actions (list,create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({ 'message': 'Hello',
                        'a_viewset': a_viewset}) #converts list/dictionary to json to response

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello sup{name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request, pk = None): #pk is primary key
        """handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self,request, pk = None): #pk is primary key
        """handle UPDATING an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self,request, pk = None): #pk is primary key
        """handle partially updating an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request, pk = None): #pk is primary key
        """handle destroying an object """
        return Response({'http_method': 'DELETE'})      
        


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class  = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() 
    authentication_classes = (TokenAuthentication,)
    # TokenAuthentication is type of authentications
    permission_classes = (permissions.UpdateOwnProfile,)

