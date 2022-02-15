from django.urls import path
from users.views import CreateTokenView, CreateUserView


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
]