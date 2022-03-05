import random

from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    articles_quantity = Article.objects.count()
    random_article_id = random.randint(1, articles_quantity)
    article = Article.objects.get(id=random_article_id)

    H1_STRING = f"""
    <h1>{article.title} ({article.id})</h1>
    """
    P_STRING = f"""
    <p>{article.content}</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)