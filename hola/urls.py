from django.contrib import admin
from django.urls import path
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.users, name='users'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('edit_user/<int:user_id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
    path('create_user/', views.create_user, name='create_user'),
    path('export_to_csv', views.export_csv, name='export_csv'),
]
