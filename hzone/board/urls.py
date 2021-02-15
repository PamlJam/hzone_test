from django.urls import path
from . import views

urlpatterns =[
    path('',views.msg_stk),
    path('upload/',views.msg_upl),
]
print('ok')