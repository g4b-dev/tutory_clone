from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_quiz, name='create_quiz'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
]
