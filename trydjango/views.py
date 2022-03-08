import random

from django.shortcuts import render
from articles.models import Article


def home_view(request, *args, **kwargs):
    random_article_id = random.randint(1, Article.objects.count())
    article = Article.objects.get(id=random_article_id)
    object_list = Article.objects.all()
    
    return render(
        request,
        template_name='home_view.html',
        context={'article': article, 'object_list': object_list}
        )