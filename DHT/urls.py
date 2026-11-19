
from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('test/', views.test, name='test'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/get', api.Dlist, name='json'),
    path('api/post', api.Dhtviews.as_view(), name='json'),
]
