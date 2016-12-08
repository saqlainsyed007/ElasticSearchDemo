from article.models import Article
from django.http import JsonResponse
from django.core import serializers


def getArticleNames(request):
    # To return whole objects

    # article_list = Article.objects.all()
    # return JsonResponse((serializers.serialize('json', article_list)), safe=False)

    # To return name and desc as [{name: name1, desc: desc1}, {name: name2, desc: desc2}, {name: name3, desc: desc3} ... ]

    # article_info = Article.objects.values('article_name', 'article_desc')
    # return JsonResponse(list(article_info), safe=False)

    article_names = Article.objects.values_list('article_name', flat=True)
    return JsonResponse(list(article_names), safe=False)
