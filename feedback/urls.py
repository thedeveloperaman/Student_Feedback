from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('thanks/', views.thanks, name='thanks'),
    path('list/', views.feedback_list, name='feedback_list'),
]
