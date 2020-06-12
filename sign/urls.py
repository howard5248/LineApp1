# HelloWord\sign\urls.py 路徑下的程式碼。
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]