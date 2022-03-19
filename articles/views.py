from webbrowser import get
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm


def article_search_view(request):
    article = None
    try:
        query = int(request.GET.get('q'))
    except:
        query = None
    if query is not None:
        article = Article.objects.get(id=query)
    context = {'object': article}
    return render(request, 'articles/search.html', context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        context['obj'] = form.save()
        context['form'] = ArticleForm()
    return render(request, 'articles/create.html', context=context)


def article_detail_view(request, id=None):
    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    context = {
        "object": article
    }
    return render(request, 'articles/detail.html', context=context)
