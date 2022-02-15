from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls 
from API import views

urlpatterns = [
    path('', views.AllMethods.as_view(), name='all-methods'),
    path('docs/', include_docs_urls(title='JobSearch-docs')),
    path('job-search/<str:query>/', views.JobSearchView.as_view(), name='jobsearch'),
    path('job-search/', views.JobSearchView.as_view(), name='jobsearch'),
    path('linkedin/<str:query>/', views.LinkedinView.as_view(), name='linkedin'),
    path('linkedin/', views.LinkedinView.as_view(), name='linkedin'),
    path('e-estekhdam/<str:query>/', views.EestekhdamView.as_view(), name='e-estekhdam'),
    path('e-estekhdam/', views.EestekhdamView.as_view(), name='e-estekhdam'),
    path('yarijob/<str:query>/', views.YarijobView.as_view(), name='yarijob'),
    path('yarijob/', views.YarijobView.as_view(), name='yarijob'),
    path('karboom/<str:query>/', views.KarboomView.as_view(), name='karboom'),
    path('karboom/', views.KarboomView.as_view(), name='karboom'),
    path('jobinja/<str:query>/', views.JobinjaView.as_view(), name='jobinja'),
    path('jobinja/', views.JobinjaView.as_view(), name='jobinja'),

    path('schema/', get_schema_view(
        title='JobSearch-schema',
        description='JobSearch-schema',
        version='1.0.0'
    ), name='openapi-schema'),

    path('users/', include('users.urls'), name='users'),
]