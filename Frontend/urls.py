from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.SearchPageView, name='search-page'),
    path('login/', views.LoginViwe, name='login'),
    path('register/', views.RegisterViwe, name='register'),
]