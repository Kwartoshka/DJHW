from django.views.generic import ListView
from django.shortcuts import render


from articles.models import Article, ArticleTag


def which_is_main(article_id, tags):
    for i, tag in enumerate(tags):
        result = ArticleTag.objects.get(article_id_id=article_id, tag_id_id=tag['id']).is_main
        if result:
            tags.pop(i)
            tags.insert(0, tag)
    return tags


def articles_list(request):
    template = 'articles/news.html'
    context_dicts = []
    data = Article.objects.all().prefetch_related('tags').order_by('-published_at')
    for article in data:
        tags = list(article.tags.all().values())
        tags = which_is_main(article.pk, tags)
        current_article = {'article': article, 'tags': tags}
        context_dicts.append(current_article)
    context = {'object_list': context_dicts}

    return render(request, template, context)
