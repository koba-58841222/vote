from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    question = Question.objects.all()
    header = ['質問内容', '選択肢1', '選択肢2', '選択肢3', '選択肢4']
    info = {
        'val': question,
        'header': header,
    }
    return render(request, 'morningApp/index.html', info)

def test(request):
    return render(request, 'morningApp/test.html', {})