from django.shortcuts import render

def home(request):
    context = {}
    response = render(request,'home.html',context)
    return response