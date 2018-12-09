from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from ContractMis import models
import time
# Create your views here.


# 写合同
def xiehetong(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            return render(request, 'xiehetong.html', {'username': request.session['NAME']})
        else:
            # POST方法提交合同
            title = request.POST['qa-cont']
            abstract = request.POST['qa-cont']
            content = '姓名：'+request.POST['cname']+'\n手机号：'+request.POST['cphone']+'\n邮箱'+request.POST['cemail']+request.POST['qa-cont']
            save_contract(request.session.get('USER'), title, abstract, content)
            return render(request, 'xiehetong.html', {'username': request.session['NAME'], 'error_msg': '提交成功'})
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 审合同
def gaihetong(request):
    username = request.session.get('USER')
    if username is not None:
        if if_access(username):
            if request.method == "GET":
                return render(request, 'gaihetong.html', {'username': request.session['NAME']})
            else:
                pass
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
                return render(request, 'hetongfanben.html', {'username': request.session['NAME']}, {'error_msg': '没有权限'})

        return render(request, 'hetongfanben.html', {'username': request.session['NAME']})
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 专利许可证合同
def zhuanlijishuxukehetong(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            return render(request, 'zhuanlijishuxukehetong.html', {'username': request.session['NAME']})
        else:
            pass
    else:
        return HttpResponseRedirect('/?user_errors=1')


# 我的合同
def my(request):
    username = request.session.get('USER')
    if username is not None:
        if request.method == "GET":
            return render(request, 'myhetong.html', {'username': request.session['NAME']})
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
            return HttpResponseRedirect('/home/')
        else:
            return render(request, 'yuehetong.html', {'warnning': '账号或密码错误'})
    else:
        print(request.GET.get('user_errors'))
        if request.GET.get('user_errors') == '1':
            return render(request, 'yuehetong.html', {'error_msg': "请先登录"})
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
    contracts = {}
    objs = models.Contract.objects.filter(username=username)
    list = []
    for item in objs:
        contract = dir()
        contract['id'] = item.id
        contract['title'] = item.title
        contract['result'] = item.results
        contract['abstract'] = item.abstract
        contract['content'] = item.content
        contract['time'] = item.time
        check = []
        objs2 = models.CheckInfo.objects.filter(contract_id=item.id)
        for item2 in objs2:
            checkinfo = dir()
            checkinfo['contract_id'] = item2.contract_id
            checkinfo['time'] = item2.time
            checkinfo['result'] = item2.results
            checkinfo['content'] = item2.content
            check.append(checkinfo)
        contract['checkInfos'] = check
        list.append(contract)
    contracts['username'] = username
    contracts['contracts'] = list

    return contracts


# 保存合同
def save_contract(username, title, abstract, content):
    result = '未审查'
    localtime = time.asctime(time.localtime(time.time()))
    models.Contract.objects.create(username=username, title=title, abstract=abstract, content=content, results=result, time=localtime)


# 保存checkInfo
def save_checkinfo(contract_id, result, content):
    localtime = time.asctime(time.localtime(time.time()))
    models.Contract.objects.create(contract_id=contract_id ,content=content, results=result, time=localtime)


# def create_warn(warntips):
#     html = "<div class='alert alert-danger' role='alert' id='alertmsg'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button><span id='alertmsg-cont'>" + warntips + "</span></div>"
#     return html
