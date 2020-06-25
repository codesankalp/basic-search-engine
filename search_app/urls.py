from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='start'),
    path('results/',views.index,name='results'),
]
