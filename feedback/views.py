from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

def feedback_form(request):
    """
    Display and handle the feedback submission form.
    GET: Shows empty form
    POST: Processes form submission
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect(reverse('feedback:thanks'))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

def thanks(request):
    """
    Display thank you page after successful feedback submission.
    Redirects to form if accessed directly.
    """
    if not messages.get_messages(request):
        return redirect('feedback:feedback_form')
    return render(request, 'feedback/thanks.html')

def feedback_list(request):
    """
    Display list of all feedback submissions ordered by newest first.
    """
    feedbacks = (Feedback.objects
                .all()
                .order_by('-created_at'))
    return render(request, 'feedback/feedback_list.html', {
        'feedbacks': feedbacks
    })