from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('', views.user_create, name='create'),
    path('<int:id>/', views.user_profile, name='user_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
