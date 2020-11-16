from django.shortcuts import render
from .forms import FeedbackForm
# Create your views here.
def Feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form':form})
