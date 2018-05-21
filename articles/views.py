from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def article_list(request):
    # return HttpResponse('Hello from Python!')
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/list.html', {'articles':articles})

def article_detail(request, slug):
	return HttpResponse(slug)
	article = Article.objects.get(slug = slug)
	return render(request, 'articles/detail.html', {'article':article})