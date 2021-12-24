from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('users/', views.users, name='users'),
	path('delete_users/<str:pk>/', views.delete_users, name="delete_users"),


]