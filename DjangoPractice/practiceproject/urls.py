from django.contrib import admin
from django.urls import path
from practiceapp import views
from practiceapp.views import Insert_author, Insert_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insert_author/',views.Insert_author,name='Insert_author'),
    path('Insert_book/',views.Insert_book,name='Insert_book'),
    path('author/',views.author,name='author'),
    path('edit_data/<int:id>/',views.edit_data, name='edit_data'),
    path('delete_data/<int:id>/',views.delete_data,name='delete_data'),
    path('book/',views.book,name='book'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register_view/',views.register_view,name='register'),
    path('',views.login_view,name ='login'),
    path('logout_view/',views.logout_view,name='logout'),
  ]