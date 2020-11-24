from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import feedback

# Create your views here.
def Feedback(request):
    print("Hello Feedback called")
    context = {
        "form":FeedbackForm
    }
    return render(request, 'feedback.html',context)

    # if request.method == 'POST':
    #     form = FeedbackForm(request.POST)

    # if form.is_valid():
    #     my_feedback = feedback(customer_name = form.cleaned_data['Your_Name'],
    #         event = form.cleaned_data['Event'],
    #         email = form.cleaned_data['Email'],
    #         details = form.cleaned_data['Details'],
    #         # happy = form.cleaned_data['Happy'],
    #         )
    #     my_feedback.save()

    # return render(request,'thanks.html')

    
    # if request.method == 'POST':
    #     form = FeedbackForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'thanks.html')
    # else:
    #     form = FeedbackForm()
    # return render(request, 'feedback.html', {'form':form})

def Save(request):

	form = FeedbackForm(request.POST)

	if form.is_valid():
		my_feedback = feedback(customer_name = form.cleaned_data['customer_name'],
			event = form.cleaned_data['event'],
			email = form.cleaned_data['email'],
			details = form.cleaned_data['details'],
			happy = form.cleaned_data['happy'],
			)
		my_feedback.save()
        
	return render(request,'thanks.html')