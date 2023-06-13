from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 6


