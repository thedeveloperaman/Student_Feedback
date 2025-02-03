from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('', lambda request: redirect('feedback:feedback_form')),
]
