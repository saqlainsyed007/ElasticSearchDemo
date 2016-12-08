from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import RequestContext, loader

def index(request):
    article_list = Article.objects.all()
    template = loader.get_template('article/index.html')
    context = RequestContext(request, {'article_list': article_list})
    # import ipdb
    # ipdb.set_trace()
    return HttpResponse(template.render(context))

def content(request, name):
    article_list = Article.objects.all()
    article_obj = Article.objects.get(article_name = name)
    template = loader.get_template('article/content.html')
    context = RequestContext(request, {'article_obj': article_obj, 'name': name, 'article_list': article_list})
    return HttpResponse(template.render(context))
