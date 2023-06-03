from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("", views.home, name="home"),
    path("room/<str:primaryKey>", views.room, name="room"),
    path("profile/<str:primaryKey>/", views.userProfile, name="user-profile"),
    path("update-user/", views.updateUser, name="update-user"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:primaryKey>", views.updateRoom, name="update-room"),
    path("delete-room/<str:primaryKey>", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:primaryKey>", views.deleteMessage, name="delete-message"),
    path("topics/", views.topicsPage, name="topics"),
    path("activity/", views.activityPage, name="activity"),
]
