# feedback_project/urls.py
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),  # Include the feedback app URLs
    path('', lambda request: redirect('feedback_form')),  # Redirect root URL to feedback form
]