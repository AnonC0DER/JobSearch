from django.urls import path 
from API import views

urlpatterns = [
    path('', views.AllMethods, name='all-methods'),
    path('job-search/<str:query>/', views.JobSearchView.as_view(), name='jobsearch'),
    path('job-search/', views.JobSearchView.as_view(), name='jobsearch'),
    path('e-estekhdam/<str:query>/', views.EestekhdamView, name='e-estekhdam'),
    path('yarijob/<str:query>/', views.YarijobView, name='yarijob'),
    path('karboom/<str:query>/', views.KarboomView, name='karboom')
]