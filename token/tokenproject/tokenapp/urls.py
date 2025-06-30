from django.urls import path
from .views import TokenWelcomeView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('welcome/', TokenWelcomeView.as_view(), name='token_welcome'),
    path('get-token/', obtain_auth_token, name='get_token'),
]