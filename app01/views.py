from django.forms import Form, widgets
from django.forms import fields
from django.shortcuts import render, redirect

from app01 import models


# 注销用户
def logout(request):
    request.session.clear()
    return redirect("/login/")


# 用户登录
def login(req):
    message = ""
    if req.method == 'POST':
        userid = req.POST.get("userid")
        password = req.POST.get("password")
        userpwd = models.UserInfo.objects.filter(userid=userid, password=password).count()
        if userpwd:
            username = models.UserInfo.objects.filter(userid=userid).values("username")
            username = username[0]["username"]
            req.session['is_login'] = True
            req.session['username'] = username
            req = redirect("/index/")
            return req
        else:
            message = "用户名或密码错误"
    return render(req, "login.html", {"msg": message})


# 权限管理（session）装饰器
def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')

    return inner


# 首页
@auth
def index(req):
    username = req.session.get("username")
    if username:
        return render(req, "index.html", {"username": username})
    else:
        return redirect("/login/")


# 用户列表
class UserForm(Form):
    userid = fields.CharField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    username = fields.CharField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    password = fields.CharField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))


# 查看用户
@auth
def user(request):
    username = request.session.get("username")
    if username:
        user_list = models.UserInfo.objects.all()
        sampletype_list = models.SampleType.objects.all()
        return render(request, "user.html",
                      {"username": username, "user_list": user_list, "sampletype_list": sampletype_list})
    else:
        return redirect("/login/")


# 添加用户
@auth
def add_user(request):
    if request.method == "GET":
        obj = UserForm()
        return render(request, 'add_user.html', {'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/user/')
        return render(request, 'add_user.html', {'obj': obj})


@auth
def del_user(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/')


@auth
def edit_user(request, nid):
    if request.method == "GET":
        row = models.UserInfo.objects.filter(id=nid).values('userid', 'username', 'password').first()
        obj = UserForm(initial=row)
        return render(request, 'edit_user.html', {'nid': nid, 'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/user/')
        return render(request, 'edit_user.html', {'nid': nid, 'obj': obj})


class ProjectForm(Form):
    project_id = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    date = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    client = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    applicant = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    project_name = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    area = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    contacts = fields.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    counterman = fields.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    customer = fields.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    plan_date_sample = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    report_agree_date = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    number_of_reports = fields.CharField(max_length=5, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    test_style = fields.CharField(max_length=5, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    report_type = fields.CharField(max_length=5, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    quality_control_report = fields.CharField(max_length=2, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    split_or_not = fields.CharField(max_length=2, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    subpackage_or_not = fields.CharField(max_length=2, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    mission_link = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    voluntary_standards = fields.CharField(max_length=255, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    collector = fields.CharField(max_length=25, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    sample_date = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    progress = fields.CharField(max_length=5, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    status_bar = fields.CharField(max_length=2, widget=widgets.TextInput(attrs={'class': 'form-control'}))


@auth
def fun1_project(request):
    username = request.session.get("username")
    if username:
        project_list = models.ProjInfo.objects.all().values('project_id', 'date', 'client',
                                                            'area', 'project_name', 'test_style',
                                                            'contacts', 'mission_link',
                                                            'voluntary_standards')
        return render(request, "fun1_project.html", {"username": username, "project_list": project_list})
    else:
        return redirect("/login/")


@auth
def fun1_addproject(request):
    if request.method == "GET":
        obj = ProjectForm()
        return render(request, 'fun1_addproject.html', {'obj': obj})
    else:
        obj = ProjectForm(request.POST)
        if obj.is_valid():
            # obj.cleaned_data # 字典
            # 数据库创建一条数据
            # print(obj.cleaned_data)
            # models.Classes.objects.create(title=obj.cleaned_data['tt'])

            models.ProjInfo.objects.create(**obj.cleaned_data)
            return redirect('/fun1_project/')
        return render(request, 'fun1_addproject.html', {'obj': obj})


@auth
def fun1_editproject(request, project_id):
    if request.method == "GET":
        row = models.ProjInfo.objects.filter(project_id=project_id).values('project_id', 'date', 'client','applicant',
            'area', 'project_name', 'contacts','counterman','customer','plan_date_sample','report_agree_date','number_of_reports',
            'test_style','report_type','quality_control_report','split_or_not','subpackage_or_not','mission_link',
                                                                           'voluntary_standards','collector','sample_date','progress','status_bar').first()
        # 让页面显示初始值
        obj = ProjectForm(initial=row)
        return render(request, 'fun1_editproject.html', {'project_id': project_id, 'obj': obj})
    else:
        obj = ProjectForm(request.POST)
        if obj.is_valid():
            models.ProjInfo.objects.filter(project_id=project_id).update(**obj.cleaned_data)
            return redirect('/fun1_project/')
        return render(request, 'fun1_editproject.html', {'project_id': project_id, 'obj': obj})


@auth
def fun1_delproject(request):
    project_id = request.GET.get('project_id')
    models.ProjInfo.objects.filter(project_id=project_id).delete()
    return redirect('/fun1_project/')


# class SampleTypeForm(Form):
#     sample_type = fields.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#
#
# @auth
# def fun21_sampletype(request):
#     sampletype_list = models.SampleType.objects.all()
#     return render(request, 'fun21_sampletype.html', {'sampletype_list': sampletype_list})
#
#
# @auth
# def fun21_addsampletype(request):
#     if request.method == "GET":
#         obj = SampleTypeForm()
#         return render(request, 'fun21_addsampletype.html', {'obj': obj})
#     else:
#         obj = SampleTypeForm(request.POST)
#         if obj.is_valid():
#             models.SampleType.objects.create(**obj.cleaned_data)
#             return redirect('/fun21_sampletype/')
#         return render(request, 'fun21_addsampletype.html', {'obj': obj})
#
#
# @auth
# def fun21_editsampletype(request, nid):
#     if request.method == "GET":
#         row = models.SampleType.objects.filter(id=nid).first()
#         obj = SampleTypeForm(initial={'sample_type': row.sample_type})
#         return render(request, 'fun21_editsampletype.html', {'nid': nid, 'obj': obj})
#     else:
#         obj = SampleTypeForm(request.POST)
#         if obj.is_valid():
#             models.SampleType.objects.filter(id=nid).update(**obj.cleaned_data)
#             return redirect('/fun21_sampletype/')
#         return render(request, 'fun21_editsampletype.html', {'nid': nid, 'obj': obj})
#
#
# @auth
# def fun21_delsampletype(request):
#     nid = request.GET.get('nid')
#     models.SampleType.objects.filter(id=nid).delete()
#     return redirect('/user/')
#
#
# class SampleForm(Form):
#     sample_id = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     stt_id = fields.IntegerField(
#         widget=widgets.Select(choices=models.SampleType.objects.values_list('id', 'sample_type'),
#                               attrs={'class': 'form-control'})
#     )
#     analysis_items = fields.CharField(max_length=220, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     standard_limit = fields.CharField(max_length=120, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     stp_id = fields.IntegerField(
#         widget=widgets.Select(choices=models.ProjInfo.objects.values_list('id', 'project_id'),
#                               attrs={'class': 'form-control'})
#     )
#
#
# @auth
# def fun2_sample(request):
#     username = request.session.get("username")
#     if username:
#         sample_list = models.SampleInfo.objects.all()
#         return render(request, "fun2_sample.html", {"username": username, "sample_list": sample_list})
#     else:
#         return redirect("/login/")
#
#
# @auth
# def fun2_addsample(request):
#     if request.method == "GET":
#         obj = SampleForm()
#         return render(request, 'fun2_addsample.html', {'obj': obj})
#     else:
#         obj = SampleForm(request.POST)
#         if obj.is_valid():
#             models.SampleInfo.objects.create(**obj.cleaned_data)
#             return redirect('/fun2_sample/')
#         return render(request, 'fun2_addsample.html', {'obj': obj})
#
#
# @auth
# def fun2_editsample(request, nid):
#     if request.method == "GET":
#         row = models.SampleInfo.objects.filter(id=nid).values('sample_id', 'stt_id', 'analysis_items',
#                                                               'standard_limit', 'stp_id').first()
#         # 让页面显示初始值
#         obj = SampleForm(initial=row)
#         return render(request, 'fun2_editsample.html', {'nid': nid, 'obj': obj})
#     else:
#         obj = SampleForm(request.POST)
#         if obj.is_valid():
#             models.SampleInfo.objects.filter(id=nid).update(**obj.cleaned_data)
#             return redirect('/fun2_sample/')
#         return render(request, 'fun2_editsample.html', {'nid': nid, 'obj': obj})
#
#
# @auth
# def fun2_delsample(request):
#     nid = request.GET.get('nid')
#     models.SampleInfo.objects.filter(id=nid).delete()
#     return redirect('/fun2_sample/')
#
#
# class ResultForm(Form):
#     rts_id = fields.IntegerField(
#         widget=widgets.Select(choices=models.SampleInfo.objects.values_list('id', 'sample_id'),
#                               attrs={'class': 'form-control'})
#     )
#     item = fields.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     analysis_method = fields.CharField(max_length=100, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     result = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     rtu_id = fields.IntegerField(
#         widget=widgets.Select(choices=models.UnitChoose.objects.values_list('id', 'unit'),
#                               attrs={'class': 'form-control'})
#     )
#     analysis_limit = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     pollute_limit = fields.CharField(max_length=20, widget=widgets.TextInput(attrs={'class': 'form-control'}))
#     rtj_id = fields.IntegerField(
#         widget=widgets.Select(choices=models.JudgeChoose.objects.values_list('id', 'judge'),
#                               attrs={'class': 'form-control'})
#     )
#
#
# @auth
# def fun3_result(request):
#     username = request.session.get("username")
#     if username:
#         result_list = models.ResultInfo.objects.all()
#         return render(request, "fun3_result.html", {"username": username, "result_list": result_list})
#     else:
#         return redirect("/login/")
#
#
# @auth
# def fun3_addresult(request):
#     if request.method == "GET":
#         obj = ResultForm()
#         return render(request, 'fun3_addresult.html', {'obj': obj})
#     else:
#         obj = ResultForm(request.POST)
#         if obj.is_valid():
#             models.ResultInfo.objects.create(**obj.cleaned_data)
#             return redirect('/fun3_result/')
#         return render(request, 'fun3_addresult.html', {'obj': obj})
#
#
# @auth
# def fun3_editresult(request, nid):
#     if request.method == "GET":
#         row = models.ResultInfo.objects.filter(id=nid).values('rts_id', 'item', 'analysis_method', 'result', 'rtu_id',
#                                                               'analysis_limit', 'pollute_limit', 'rtj_id').first()
#         # 让页面显示初始值
#         obj = ResultForm(initial=row)
#         return render(request, 'fun3_editresult.html', {'nid': nid, 'obj': obj})
#     else:
#         obj = ResultForm(request.POST)
#         if obj.is_valid():
#             models.ResultInfo.objects.filter(id=nid).update(**obj.cleaned_data)
#             return redirect('/fun3_result/')
#         return render(request, 'fun3_editresult.html', {'nid': nid, 'obj': obj})
#
#
# def fun3_delresult(request):
#     nid = request.GET.get('nid')
#     models.ResultInfo.objects.filter(id=nid).delete()
#     return redirect('/fun3_result/')
