from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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