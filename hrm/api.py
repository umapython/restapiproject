from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class userlist(APIView):
    def get(self,request):
        model=Users.objects.all()
        serializer = Usersserializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Usersserializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class userdetail(APIView):
    def get(self,request,employee_id):
        model=Users.objects.all()
        serializer = Usersserializer(model)
        return Response(serializer.data)

    def put(self,request,employee_id):
        serializer = Usersserializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)