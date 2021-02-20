from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('first_view/<int:user_id>', views.first_view, name='firstView'),
    path('list_publishers/', views.list_publishers, name='list_publishers'),
    path('new_publisher/', views.new_publisher, name='new_publisher'),
    path('list_users/', views.list_users, name='list_users'),
    path('new_user/', views.new_user, name='new_user'),
]
