from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from profiles_api import serializers

from profiles_api import permissions

from rest_framework.authtoken.views import  ObtainAuthToken

from rest_framework.settings import api_settings
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication;


from profiles_api import models

# Create your views here.

class UserView(APIView):


    serailized_input = serializers.InputSerializer

    def get(self,request):
        
        return Response({"message":"No user found"})
    

    def post(self,request):
        
        print("hih"+request.data)
        serilizer = self.serailized_input(data=request.data)

        if serilizer.is_valid():
            name = serilizer.validated_data.get('name')
            res = "hellow"+name
            return Response({"message":res})
        else:
          
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfilSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication ,)
    permission_classes = (permissions.UpdateProfile,)
    filter_backends =  (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLogin(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES