from django.shortcuts import render, redirect
from django.http import Http404
from .models import Question

# Create your views here.

def index(request):
    question = Question.objects.all()
    info = {
        'val': question,
    }
    return render(request, 'morningApp/index.html', info)

def test(request):
    return render(request, 'morningApp/test.html', {})

def vote_a(request, pk):
    question = Question.objects.get(pk=pk)
    question.total_votes += 1
    question.votes_a += 1
    question.save() # 保存をする
    
    question.per_a =  (question.votes_a / question.total_votes) * 100
    question.per_b =  (question.votes_b / question.total_votes) * 100
    question.per_c =  (question.votes_c / question.total_votes) * 100
    question.per_d =  (question.votes_d / question.total_votes) * 100
    question.save() # 保存をする
    return redirect('index')

def vote_b(request, pk):
    question = Question.objects.get(pk=pk)
    question.total_votes += 1
    question.votes_b += 1
    question.save() # 保存をする
    
    question.per_a =  (question.votes_a / question.total_votes) * 100
    question.per_b =  (question.votes_b / question.total_votes) * 100
    question.per_c =  (question.votes_c / question.total_votes) * 100
    question.per_d =  (question.votes_d / question.total_votes) * 100
    question.save() # 保存をする
    return redirect('index')

def vote_c(request, pk):
    question = Question.objects.get(pk=pk)
    question.total_votes += 1
    question.votes_c += 1
    question.save() # 保存をする
    
    question.per_a =  (question.votes_a / question.total_votes) * 100
    question.per_b =  (question.votes_b / question.total_votes) * 100
    question.per_c =  (question.votes_c / question.total_votes) * 100
    question.per_d =  (question.votes_d / question.total_votes) * 100
    question.save() # 保存をする
    return redirect('index')

def vote_d(request, pk):
    question = Question.objects.get(pk=pk)
    question.total_votes += 1
    question.votes_d += 1
    question.save() # 保存をする
    
    question.per_a =  (question.votes_a / question.total_votes) * 100
    question.per_b =  (question.votes_b / question.total_votes) * 100
    question.per_c =  (question.votes_c / question.total_votes) * 100
    question.per_d =  (question.votes_d / question.total_votes) * 100
    question.save() # 保存をする
    return redirect('index')