from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import Http404, response
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from blog.models import Article
from blog.models import ArticleType

def write(request):
    user = request.user
    context = {}

    if not user.is_authenticated:
        raise Http404('None')

    if request.method == 'GET' :
        context ['types'] = ArticleType.objects.filter(author = user)
        response =  render(request,'write.html',context)
        return response

    if request.method == 'POST' :
        title =  request.POST.get('title','')
        content = request.POST.get('content','')
        type =  request.POST.get('type','')    
        if not type:
            context = {'status' : 'NONE'}
            return JsonResponse(context)

        if title and content:
            new_article = Article()
            new_article.type = get_object_or_404(ArticleType,title = type)
            new_article.author = user
            new_article.title = title
            new_article.content = content
            new_article.save()
            context = {'status' : 'SUCCESS'}
        else:
            context = {'status' : 'NULL'}

        return JsonResponse(context)

def register(request):
    if request.user.is_authenticated:
        raise Http404('None')

    context = {}
    if request.method == 'GET' :
        response = render(request,'register.html',context)
        return response

    if request.method == 'POST' :
        
        un = request.POST.get('un','')
        pw = request.POST.get('pw','')
        re = request.POST.get('re','')

        if not 5<len(un)<10:
            context['status'] = '5<len(un)<10'
        elif not 5<len(pw)<10:
            context['status'] = '5<len(pw)<10'
        elif pw!=re:
        # 输入不一致
            context['status'] = 'not consistent'
        elif User.objects.filter(username= un).exists():
        # 用户已存在
            context['status'] = 'user already exists'
        else:
            context['status'] = 'SUCCESS'
            
            new_user = User.objects.create_user(un,None,pw)
            new_user.save()

            login(request,new_user)

        return JsonResponse(context)


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
    if not request.COOKIES.get(str(request.user.id) + 'browse'):
        id_user.browse += 1
        id_user.save()
    context = {}
    articles = Article.objects.filter(author = id_user)
    context['id_user'] = id_user
    context['articles'] = articles
    
    response = render(request,'room.html',context)
    response.set_cookie(str(request.user.id) + 'browse','1',max_age=3)
    return response

def update(request):
    context = {}
    response = render(request,'update.html',context)
    return response