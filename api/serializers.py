from rest_framework import exceptions
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserSerialize(ModelSerializer):
    class Meta:
        model= User
        fields="__all__"

        extra_kwargs={
            "username":{
                "required":True,
                "max_length":8,
                "min_length":2,
                "error_messages":{
                    "required":"用户名不能为空哟",
                    "max_length":"你是俄罗斯人嘛，名字那么长",
                    "min_length":"名字太短了哟",
                }
            },
            "password":{
                "required": True,
                "min_length": 2,
                "error_messages":{
                    "required": "密码不能为空哟",
                    "min_length": "密码太短了哟",
                }
            },
            "re_password":{
                "required": True,
                "error_messages":{
                    "required": "确认密码不能为空哟",
                }
            },
            "real_name":{
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "真实姓名不能为空哟",
                    "min_length": "真实姓名太短了哟",
                }
            },
        }
    def validate(self, attrs):
        username=attrs.get("username")
        password=attrs.get("password")
        re_password=attrs.get("re_password")
        print(re_password)
        res=User.objects.filter(username=username).first()
        if res:
            raise exceptions.ValidationError("用户名已存在，请重新输入")
        else:
            if password != re_password:
                raise exceptions.ValidationError("两次密码不一致，请重新输入")
            return attrs

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields = "__all__"
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "max_length": 8,
                "min_length": 2,
                "error_messages": {
                    "required": "名字不能为空哟",
                    "max_length": "你是俄罗斯人嘛，名字那么长",
                    "min_length": "名字太短了哟",
                }
            },
        }