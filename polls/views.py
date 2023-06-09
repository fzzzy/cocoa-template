

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/details.html', context)

def results(_request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(_request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)

