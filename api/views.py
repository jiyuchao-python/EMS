from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.views import APIView

from api.models import User, Employee
from api.serializers import UserSerialize, EmployeeSerializer
from utils.response import APIResponse


class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        request_data=request.data
        print(request_data)
        serializer=UserSerialize(data=request_data)
        print("okok")
        serializer.is_valid(raise_exception=True)
        res=serializer.save()
        return APIResponse(200,True,results=UserSerialize(res).data)
    def get(self,request,*args,**kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        res=User.objects.filter(username=username,password=password).first()
        print(res)
        if res:
            data = UserSerialize(res).data
            return APIResponse(200,True,results=data)
        return APIResponse(400, False)

class EmployeeView(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        pk=kwargs.get("id")
        if pk:
            return APIResponse(200, True,results=pk)
        self_list=self.list(request, *args, **kwargs)
        return APIResponse(200, True,results=self_list.data)
    def post(self,request, *args, **kwargs):
        print(request.data)
        res=self.create(request, *args, **kwargs)
        return APIResponse(200, True,results=res.data)
    def delete(self,request, *args, **kwargs):
        pk=kwargs.get("id")
        print(pk)
        # res=self.destroy(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)
        # return APIResponse(http_status=status.HTTP_204_NO_CONTENT)
        # res = Employee.objects.get(id=pk).delete()
        # return APIResponse(200, True,results="ok")
    def put(self,request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)
