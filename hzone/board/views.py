from django.shortcuts import render
from .models import Message
from django.http import Http404
from django.http import JsonResponse
from django.core.paginator import Paginator

def msg_stk(request):
    context = {}
    if request.method == 'GET':
        msgs = Message.objects.all()
        paginator = Paginator(msgs,4)
        # 分页设置
        n = request.GET.get("page",1)
        # 获取页数
        if int(n) > paginator.num_pages:
            raise Http404('None')
        p = paginator.get_page(n)
        # 获取页面
        context['msgs'] = p
        return render(request,'stk.html',context)

    
def msg_upl(request):
    user = request.user
    if user.is_authenticated and request.method == 'POST':
        text = request.POST.get('text')
        if text:
            newmsg = Message()
            newmsg.content = text
            newmsg.author = user
            newmsg.save()
            context = {
                'status' :"SUCCESS",
            }
        else:
        # 提交文本为空
            context = {
                'status' : 'NULL'
            }
        return JsonResponse(context)
    else:
        return Http404('None')