from django.shortcuts import render
from user.models import User
from django.shortcuts import redirect
from django.db.models import Q
# 引入 Q 对象
def home(request):
    context = {}
    response = render(request,'home.html',context)
    return response

def search(request):
    
    context = {}
    wds = request.GET.get('wd').strip()
    # 截去空格
    conditions = None
    # 筛选条件
    for wd in wds.split():
    # 按照空格分词
        if conditions == None:
            conditions = Q(username__icontains = wd)
        else:
            conditions |= Q(username__icontains = wd)
    if conditions !=None:
        us = User.objects.filter(conditions)
        context['us'] = us
        response = render(request,'search_result.html',context)
        return response
    else:
        referer = request.META.get("HTTP_REFERER",'/')
        return redirect(referer)