from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, Comment

class ArticleDetailTestCase(TestCase):

    def setUp(self):
    user = User.objects.create(username='testuser')
    self.article = Article.objects.create(
        title='Test Article',
        content='This is a test article',
        author=user
    )

    def test_get_article_detail(self):
        url = reverse('article_detail', args=[self.article.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.comments.first().content)

    def test_post_comment(self):
        url = reverse('article_detail', args=[self.article.slug])
        comment_data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'content': 'New comment'
        }
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, comment_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, comment_data['content'])
        self.assertEqual(self.article.comments.count(), 2)

class CommentDeleteViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title='Test Article', content='This is a test article')
        self.comment = Comment.objects.create(article=self.article, name='Test User', email='test@example.com', content='Test comment')

    def test_delete_comment(self):
        url = reverse('comment_delete', args=[self.comment.id])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('article_detail', args=[self.article.slug]))
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())