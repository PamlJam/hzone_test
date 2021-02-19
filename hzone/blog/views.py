from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article

def blog_list(requset):
    if requset.method == 'GET':
        articles = Article.objects.all()
        context = {}
        context ['articles'] = articles
        context ['pos'] = requset.session.get('pos',default =  '0')
        # 取出位置记录 默认值为0
        requset.session['pos'] = requset.GET.get('pos','0')
        # 记录实时位置
        response = render(requset,'list.html',context)
        return response

def blog_detail(requset,article_pk):
    article = get_object_or_404(Article,pk = article_pk)
    context = {}    
    context ['article'] = article
    response = render(requset,'detail.html',context)
    return response