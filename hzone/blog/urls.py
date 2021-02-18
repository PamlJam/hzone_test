from django.urls import path
from . import views

urlpatterns =[
    path('',views.blog_list),

    path('<int:article_pk>/',views.blog_detail),
]