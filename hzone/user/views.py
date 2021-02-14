from django.shortcuts import render
from django.http import HttpResponse
def upload_icon(request):
    if request.method == 'POST':
        icon = request.FILES.get('icon', None)
        # 读取表单文件信息
        if icon:
            request.user.icon = icon
            # 更改
            request.user.save()
            # 保存
            return HttpResponse('seccess')
        else:
            return HttpResponse('error')

def room(request):
    context = {}
    response = render(request,'room.html',context)
    return response

def upload(request):
    context = {}
    response = render(request,'upload.html',context)
    return response