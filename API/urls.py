from django.urls import path 
from API import views

urlpatterns = [
    path('', views.AllMethods, name='all-methods'),
    path('e-estekhdam/<str:query>/', views.EestekhdamView, name='e-estekhdam'),
    path('yarijob/<str:query>/', views.YarijobView, name='yarijob')
]