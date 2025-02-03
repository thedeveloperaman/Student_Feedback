from django.db import models

class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    feedback_text = models.TextField()
    roll_number = models.IntegerField(null=True)
    contact_number = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Feedback from {self.student_name}"

    class Meta:
        ordering = ['-created_at']
        get_latest_by = 'created_at'