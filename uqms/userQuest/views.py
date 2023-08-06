from django.http import HttpResponse
from django.shortcuts import render
from userQuest.models import User, Question

def hello(request):
    users = User.objects.all()
    questions = Question.objects.all()
    return render(request, 'userQuest/hello.html',
                  {'1stuser_name': users[0], '1stquestion_name':questions[0]},
                  )
