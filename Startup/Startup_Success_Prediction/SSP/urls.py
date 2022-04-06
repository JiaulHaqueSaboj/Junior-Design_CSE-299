from django.urls import path

from . import views
app_name = "SSP"

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name="signup"),
    path('', views.loginPage, name="loginPage"),
    path("logout", views.logout_request, name="logout"),

]
