from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

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


