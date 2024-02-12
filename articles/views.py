from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Article
from .forms import ArticleForm

# Create your views here.


def home_view(request, *args, **kwargs):
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        'object': article_obj
    }
    return render(request, 'articles/detail.html', context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_object = Article.objects.create(title=title, content=content)
        article_object = form.save()
        context['form'] = ArticleForm()     # Empties the forms
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/create.html', context)


def article_search_view(request):
    query_dict = request.GET    # This is a dictionary

    try:
        query = query_dict.get('q')
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        'object': article_obj
    }
    return render(request, 'articles/search.html', context)
