from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'create/$', views.article_create, name='create'),
    path("<slug:slug>/", views.article_detail, name="detail"),
]