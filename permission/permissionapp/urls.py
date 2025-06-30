from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from permissionapp.views import *

urlpatterns=[
    path('articles/',ArticleListView.as_view()),
    path('articles/<int:pk>/',ArticleDetailView.as_view()),
    path('articles/<int:pk>/update/',ArticleUpdateView.as_view()),
    path('articles/<int:pk>/delete/',ArticleDeleteView.as_view()),
    path('get-token/',obtain_auth_token),


]