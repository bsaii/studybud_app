from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout_user"),
    path('register/', views.register_page, name="register_page"),
    path('profile/<int:pk>/', views.user_profile, name="user_profile"),
    path('update_user/', views.update_user, name="update_user"),

    path('', views.home, name="home"),
    path('room/<int:pk>/', views.room, name="room"),

    path('create_room/', views.create_room, name="create_room"),
    path('update_room/<int:pk>/', views.update_room, name="update_room"),
    path('delete_room/<int:pk>/', views.delete_room, name="delete_room"),
    path('delete_message/<int:pk>/', views.delete_message, name="delete_message"),

    path('topics/', views.topics_page, name="topics_page"),
    path('activity/', views.activity_page, name="activity_page"),
]
