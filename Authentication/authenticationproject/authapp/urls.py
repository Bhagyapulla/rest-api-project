from django.urls import path
from .views import WelcomeView

urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='welcome'),
]