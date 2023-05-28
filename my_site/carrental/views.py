from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm
# Create your views here.

def feedback_view(request):

    if request.POST:
        # review = request.POST["review"]
        # stars = int(request.POST["stars"])
        # models.Feedback.objects.create(review=review, stars=stars).save()
        # return redirect(reverse('carrental:thanks'))
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cdata = form.cleaned_data
            review = cdata["review"]
            stars = int(cdata["stars"])
            models.Feedback.objects.create(review=review, stars=stars).save()
            return redirect(reverse('carrental:thanks'))
    else:
        form = ReviewForm()
    return render(request, 'carrental/rental_review.html', context={"form": form})

def thankyou_view(request):
    review = models.Feedback.objects.all()
    print(f"Review : {review}")
    last_review = review.last()
    context = {
        "review": last_review
    }
    return render(request, 'carrental/thankyou.html', context=context)