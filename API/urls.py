from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls 
from API import views

urlpatterns = [
    path('', views.AllMethods, name='all-methods'),
    path('docs/', include_docs_urls(title='JobSearch-docs')),
    path('job-search/<str:query>/', views.JobSearchView.as_view(), name='jobsearch'),
    path('job-search/', views.JobSearchView.as_view(), name='jobsearch'),
    path('linkedin/<str:query>/', views.LinkedinView, name='linkedin'),
    path('e-estekhdam/<str:query>/', views.EestekhdamView, name='e-estekhdam'),
    path('yarijob/<str:query>/', views.YarijobView, name='yarijob'),
    path('karboom/<str:query>/', views.KarboomView, name='karboom'),
    path('jobinja/<str:query>/', views.JobinjaView, name='jobinja'),

    path('schema/', get_schema_view(
        title='JobSearch-schema',
        description='JobSearch-schema',
        version='1.0.0'
    ), name='openapi-schema'),
]