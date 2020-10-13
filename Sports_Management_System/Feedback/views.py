from django.shortcuts import render
from .forms import FeedbackForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'Feedback/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'Feedback/feedback.html', {'form':form})
