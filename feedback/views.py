from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

def feedback_thanks_view(request):
    return render(request, 'feedback/thanks.html')

def feedback_list_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})