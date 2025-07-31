from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview = [
            'Discipline is the key to success',
            'Hardwork is a part of the path',
            'Luck is sometimes more important',
            ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
    
    def post(self,request):
        """Reads a request and respones with a name field"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST 
            )
    

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    #get
    def list(self,request):
        """Test hello message"""
        a_viewset = [
            'Uses actions(methods) like list,create,update,retrieve and partial_update',
            'Automatically maps to URLs using routers'
            'Provides more functionnality with less code'
        ]

        return Response({'message':a_viewset})
    
    def create(self,request):
        """Reads a request and respones with a name field"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST 
            )
    
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'Http_method':'GET'})
    
    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'Http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})