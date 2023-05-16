from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serilizers import *
from django.contrib.auth import authenticate
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions

# Create your views here.


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer

    def get(self, request, *args, **kwargs):
        try:
            response={"status":status.HTTP_400_BAD_REQUEST,"message":"Fetching Users Details are  Failed"}
            all_user = User.objects.all()
            serializer = self.serializer_class(all_user, many=True)
            response["status"] = status.HTTP_200_OK
            response["message"] = " Users Details fetched successfully"
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            

    def post(self,request,format=None):    
        response={"status":status.HTTP_400_BAD_REQUEST,"message":"User Creation Failed"}
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            response["status"] = status.HTTP_201_CREATED
            response["message"] = "Registration Successfull"
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def get(self,request,**kwargs):
        try:
            response={"status":status.HTTP_400_BAD_REQUEST,"message":"User with this Id is not Exist"}
            id = kwargs.get("id")
            user = User.objects.get(id=id)
            serializer =self.serializer_class(user)
            response["status"] = status.HTTP_200_OK
            response["message"] = " User Details fetched successfully"
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)     