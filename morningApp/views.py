from django.shortcuts import render, redirect
from django.http import Http404
from django.http.response import JsonResponse
from .models import Question
from .forms import QuestionForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# Create your views here.

def index(request):
    question = Question.objects.all().order_by('-id')
    keyword = request.GET.get('keyword')

    if keyword:
        question = Question.objects.filter(
                 Q(contents__icontains=keyword)
               )
    page_obj = paginate_query(request, question, settings.PAGE_PER_ITEM)   # ページネーション
    return render(request, 'morningApp/index.html', {'page_obj': page_obj, 'site_name':settings.SITE_NAME})

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

def create(request):
    form = QuestionForm()
    
    context = {
        'questionForm': form,
    }
    return render(request, 'morningApp/create.html', context)

def addQuestion(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        aaa = QuestionForm(request.POST)
        if aaa.is_valid():
            aaa.save()
    return redirect('index')

def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginatot.page(paginator.num_pages)
    return page_obj