from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request, *args, **kwargs):
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "content": article_obj.content,
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
