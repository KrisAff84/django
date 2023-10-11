from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


# The get_object_or_404 method takes a Django model as it's first
# argument and an arbitrary number of keyword arguments, which it
# passes to the get() function of the model's manager. It raises
# Http404 if the object doesn't exist, getting rid of the need to 
# use try-except blocks.

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


