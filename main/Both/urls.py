from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/',views.inscription_views,name='inscription'),
    path('login/',views.login_views,name='login'),
    path('informations/',views.informations_views,name='Informations'),
    path('contact/',views.contact_views,name='contact'),
    
]
