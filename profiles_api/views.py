from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview = [
            'Discipline is the key to success',
            'Hardwork is a part of the path',
            'Luck is sometimes more important',
            ]
        return Response({'message':'Hello!','an_apiview':an_apiview})