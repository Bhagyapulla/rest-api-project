"""
URL configuration for formproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from formapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_view/',views.register_view,name='register'),
    path('login_view/',views.login_view,name='login'),
    path('logout_view/',views.logout_view,name='logout'),
    path('insert_author/',views.insert_author,name='insert_author'),
    path('insert_book/',views.insert_book,name='insert_book'),
    path('book_author/',views.book_author,name='book_author'),
    path('edit_book/<int:book_id>',views.edit_book,name='edit_book'),
    path('del_book/<int:book_id>',views.del_book,name='del_book'),
    path('edit_author/<int:auth_id>',views.edit_author,name='edit_author'),
    path('del_author/<int:auth_id>',views.del_author,name='del_author'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
