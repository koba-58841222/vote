from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.index, name='index'),
    path('<int:pk>/vote_a/', views.vote_a, name='vote_a'),
    path('<int:pk>/vote_b/', views.vote_b, name='vote_b'),
    path('<int:pk>/vote_c/', views.vote_c, name='vote_c'),
    path('<int:pk>/vote_d/', views.vote_d, name='vote_d'),
]