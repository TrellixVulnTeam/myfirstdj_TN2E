from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def articles(request):
    # return HttpResponse('Hello from Python!')
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/list.html', {'articles':articles})