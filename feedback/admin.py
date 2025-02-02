from django.contrib import admin

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'feedback_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student_name', 'feedback_text')
    readonly_fields = ('created_at',)

admin.site.register(Feedback, FeedbackAdmin)