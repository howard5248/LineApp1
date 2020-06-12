from django.urls import path
from . import views

urlpatterns = [
    path('punch_in', views.punch_in.as_view(), name='punch_in'),
    path('postLocation', views.postLocation),
    path('getUserName', views.getUserName)
    # path('postLocation', postLocation.postLocation)
]