from django.urls import path
from . import views
urlpatterns =[
    path('',views.room),
    path('upload/',views.upload),
    path('upload_icon/',views.upload_icon),
]