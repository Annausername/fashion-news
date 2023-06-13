from . import views
from django.urls import path

from .views import (
    ArticleList,
    ArticleDetail,
    ArticleLike,
    UpvoteArticleView,
    DownvoteArticleView,
    CommentDeleteView,
)

urlpatterns = [
    path("", views.ArticleList.as_view(), name="home"),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('posts/<int:article_id>/upvote/', UpvoteArticleView.as_view(), name='upvote_article'),
    path('posts/<int:article_id>/downvote/', DownvoteArticleView.as_view(), name='downvote_article'),
    path('comment/delete/<int:comment_id>/', CommentDeleteView.as_view(), name='comment_delete'),
]
