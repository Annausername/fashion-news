from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 6

class ArticleDetail(View):
    
    def get(self, request, slug, *args, **kwags):
        queryset = Article. objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = arrticle.filter(approved=True).order_by('-created_at')
        liked = False
        if article.likes.filter(id=self.request.userr.id).exists():
            liked = True

        return render(
            request,
            "article_detail.html"
            {
                "article": article
                "comments": comments
                "liked": liked
            },
        )
