from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'feedback_text', 'email', 'roll_number','contact_number','subject','created_at')
    search_fields = ('student_name', 'email', 'feedback_text')
    list_filter = ('created_at',)