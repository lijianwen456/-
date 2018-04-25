import re

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def register(request):
    return render(request, "register.html")


def do_register(request):
    # 获取post 请求参素
    username=request.POST.get("username")
    password = request.POST.get("password")
    password2 = request.POST.get("password2")
    email = request.POST.get("email")
    allow = request.POST.get("allow")  #用户勾选，ON
    # TODO 验证参数合法性
    # 判断参数不能为空
    if not all([username,password,password2,email]):
        return render(request,"register.html",{'errmsg':'参赛不能为空'})
    # 密码是否一致
    if password != password2:
        return render(request, "register.html", {'errmsg': '密码不一致'})
    # 邮箱合法
    if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$",email):
        return render(request, "register.html", {'errmsg': '邮箱不合法'})
    # 用户协议
    if allow != "on":
        return render(request, "register.html", {'errmsg': '请勾选协议'})

    # 处理业务：保存用户到数据库表中
    # 判断用户是否存在
    # 修改用户状态为未激活

    # todo 发送激活邮件



    return HttpResponse('注册成功，进入登陆界面')
