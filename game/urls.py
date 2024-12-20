from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game'),
    path('submit-time/', views.submit_time_view, name='submit_time')
]