from django.shortcuts import render
from .models import Message
from django.http import Http404
from django.http import JsonResponse

def msg_stk(request):
    context = {}
    msgs = Message.objects.all()
    context['msgs'] = msgs
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