from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def articles(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'articles/list.html')