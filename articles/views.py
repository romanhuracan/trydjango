from django.shortcuts import render

from articles.models import Article


def article_detail_view(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    context = {
        "object": article
    }
    return render(request, 'articles/detail.html', context=context)
