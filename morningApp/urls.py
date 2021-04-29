from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.index, name='index'),
    path('<int:pk>/vote_a/', views.vote_a, name='vote_a'),
    path('<int:pk>/vote_b/', views.vote_b, name='vote_b'),
    path('<int:pk>/vote_c/', views.vote_c, name='vote_c'),
    path('<int:pk>/vote_d/', views.vote_d, name='vote_d'),
    path('createQ/', views.createQ, name='createQ'),
    path('add', views.addQuestion, name='addQuestion'),
    path("login/", auth_views.LoginView.as_view(template_name="morningApp/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", views.signup, name="signup"),
    path('popular/', views.popular, name='popular'),
    path('trend/', views.trend, name='trend'),
]
