from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse

def log_in(request):
    
    if request.user.is_authenticated:
        raise Http404('None')
    elif request.method == 'POST':
        un = request.POST.get('un','')
        pw = request.POST.get('pw','')
        user = authenticate(request, username=un, password=pw)
        context = {}
        if user is not None:
            context['status'] = 'SUCCESS'
            login(request, user)
        else:
            context['status'] = 'ERROR'
        return JsonResponse(context)
    else:
        return render(request,'login.html',{})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        raise Http404('None')

def upload(request):
    if request.method == 'POST':
        user = request.user
        icon = request.FILES.get('icon')
        # 读取表单文件信息
        motto = request.POST.get('motto')

        email = request.POST.get('email')

        if icon:
            user.icon = icon
        if motto:
            user.motto = motto
        if email:
            user.email = email
        user.save()

        return render(request,'update.html',{})


def room(request,user_id):
    id_user = get_object_or_404(User,id = user_id)
    context = {}
    context['id_user'] = id_user
    
    response = render(request,'room.html',context)
    return response


def update(request):
    context = {}
    response = render(request,'update.html',context)
    return response