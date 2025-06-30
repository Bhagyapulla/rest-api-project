from django.urls import path
from sessionapp.views import SessionWelcomeView

urlpatterns = [
    path("welcome/", SessionWelcomeView.as_view())
]