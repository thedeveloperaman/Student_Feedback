# feedback/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_form'),
    path('thanks/', views.feedback_thanks_view, name='feedback_thanks'),
    path('list/', views.feedback_list_view, name='feedback_list'),
]