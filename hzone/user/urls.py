from django.urls import path
from . import views
urlpatterns =[
    path('<int:user_id>',views.room),
    path('update/',views.update),
    # 信息编辑页面
    path('upload/',views.upload),
    # 提交按钮
    path('log_out/',views.log_out),
    # 注销按钮
    path('log_in/',views.log_in),
    # 登录按钮

]