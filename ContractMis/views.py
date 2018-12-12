from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
from ContractMis import models
import time

# Create your views here.

from ContractMis.models import Contract


# 写合同
def xiehetong(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            return render(request, 'xiehetong.html', {'username': request.session['NAME']})
        else:
            # POST方法提交合同
            # title = request.POST['qa-cont']
            # abstract = request.POST['qa-cont']
            content = request.POST['qa-cont']
            cname = request.POST['cname']
            cphone = request.POST['cphone']
            cemail = request.POST['cemail']
            save_contract(request.session.get('USER'), cname, cphone, cemail, content)
            return render(request, 'xiehetong.html', {'username': request.session['NAME'], 'error_msg': '提交成功'})
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 审合同
def gaihetong(request):
    username = request.session.get('USER')
    if username is not None:
        if if_access(username):
            if request.method == "GET":
                contracts = Contract.objects.all()
                return render(request, 'gaihetong.html', {'username': request.session['NAME'],
                                                          'contracts': contracts})
            else:
                price = request.POST['aprice']
                cname = request.POST['cname']
                cphone = request.POST['cphone']
                cemail = request.POST['cemail']
                qa_cont = request.POST['qa-cont']
                id = request.POST['id']
                save_checkinfo(id, cname, cphone, cemail, price, qa_cont)
                return render(request, 'gaihetong.html', {'username': request.session['NAME'], 'warnning': '提交成功'})
        return HttpResponseRedirect('/home/?user_errors=2')
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 合同范本（智能合同）
def home(request):
    username = request.session.get('USER')

    if username is not None:
        # 用户没有审查合同权限
        if request.method == 'GET':
            user_errors = request.GET.get('user_errors')
            if user_errors == '2':
                return render(request, 'hetongfanben.html', {'username': request.session['NAME'], 'warnning': '没有权限'})

        return render(request, 'hetongfanben.html', {'username': request.session['NAME']})
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 专利许可证合同
def zhuanlijishuxukehetong(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            return render(request, 'diy/zhuanlijishuxukehetong.html', {'username': request.session['NAME']})
        else:
            pass
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 我的合同
def my(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            contracts = get_contract_list(username)
            return render(request, 'myhetong.html', {'username': request.session['NAME'],
                                                     'contracts': contracts})
        else:
            pass
    else:
        return HttpResponseRedirect('/?user_errors=1')


# login
def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        pwd = request.POST['pwd']
        name = if_user(username, pwd)
        if name is not None:
            request.session['USER'] = username
            request.session['NAME'] = name
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'yuehetong.html', {'warnning': '账号或密码错误'})
    else:
        print(request.GET.get('user_errors'))
        if request.GET.get('user_errors') == '1':
            return render(request, 'yuehetong.html', {'warnning': "请先登录"})
        return render(request, 'yuehetong.html')


def logout(request):
    username = request.session.get('USER')
    if username is not None:
        request.session['USER'] = False
        del request.session['USER']
    return HttpResponseRedirect('/')


# 判断用户是否存在 密码是否正确
def if_user(username, password):
    user = models.User.objects.filter(username=username).first()
    if user is not None:
        user_pwd = user.password
        if user_pwd == password:
            return user.name
        return None
    return None


# 判断用户有无进入改合同权限
def if_access(username):
    user = models.User.objects.filter(username=username).first()
    if user.level > 2:
        return True
    return False


# 获取合同列表
def get_contract_list(username):
    objs = models.Contract.objects.filter(username=username)
    contracts = []
    for item in objs:
        contract = dict()
        contract['contract_id'] = item.contract_id
        contract['title'] = item.title
        contract['result'] = item.results
        contract['name'] = item.name
        contract['content'] = item.content
        contract['phone'] = item.phone
        contract['price'] = item.price
        contract['email'] = item.email
        contract['time'] = item.time
        contract['username'] = username
        contracts.append(contract)
    return contracts


# 保存合同
def save_contract(username, cname, cphone, cemail, content, title="默认", abstract="",price=3000):
    result = '未审查'
    models.Contract.objects.create(username=username, name=cname, phone=cphone, email=cemail, title=title,
                                   abstract=abstract, content=content, results=result, price=price
                                   )


# 保存checkInfo
def save_checkinfo(contract_id, cname, cphone, ceamil, content, result="通过", price=3000):
    models.CheckInfo.objects.create(contract_id=contract_id,
                                    content=content,
                                    results=result,
                                    name=cname,
                                    phone=cphone,
                                    email=ceamil,
                                    price=price)
    models.Contract.objects.filter(contract_id=contract_id).update(results='通过审查')


def pricing_view(request):
    return render(request, 'service/pricing.html')


def agreement_view(request):
    return render(request, 'service/agreement.html')
