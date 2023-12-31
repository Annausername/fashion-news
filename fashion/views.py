from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm

class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by("-upvotes")
    template_name = "index.html"
    paginate_by = 6

class ArticleDetail(View):
    
    def get(self, request, slug, *args, **kwags):
        queryset = Article. objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('-created_at')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
    def post(self, request, slug, *args, **kwags):
        queryset = Article. objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('-created_at')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
            },
        )

class ArticleLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))    

class UpvoteArticleView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article.upvote()
        return redirect('home')

class DownvoteArticleView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article.downvote()
        return redirect('home')

from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Comment

class CommentDeleteView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('article_detail', slug=comment.article.slug)


