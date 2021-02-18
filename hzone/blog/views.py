from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
from .models import ArticleType


def blog_list(requset):
    articles = Article.objects.all()
    context = {}
    context ['articles'] = articles

    response = render(requset,'list.html',context)
    
    return response


def blog_detail(requset,article_pk):

    article = get_object_or_404(Article,pk = article_pk)

    context = {}    

    context ['article'] = article

    response = render(requset,'detail.html',context)

    return response