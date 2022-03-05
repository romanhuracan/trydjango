import random

from django.shortcuts import render
from articles.models import Article


def home_view(request):
    random_article_id = random.randint(1, Article.objects.count())
    article = Article.objects.get(id=random_article_id)

    return render(
        request,
        template_name='home_view.html',
        context={'article': article}
        )