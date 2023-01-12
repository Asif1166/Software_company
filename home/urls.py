

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hom, name='home'),
    path('layout/', views.layout, name='layout'),
    path('price/', views.price, name='price'),
    path('technology/', views.technology, name='technology'),
    path('job/', views.job, name='job'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('index/', views.index, name='index'),
    
    path('layout1/', views.layout1, name='layout1'),
    
    
    
    
]