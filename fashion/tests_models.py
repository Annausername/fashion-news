from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Comment

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create a test article
        Article.objects.create(
            title='Test Article',
            slug='test-article',
            author=test_user,
            content='This is a test article content',
        )

    def test_article_title(self):
        article = Article.objects.get(slug='test-article')
        expected_title = 'Test Article'
        self.assertEqual(article.title, expected_title)

    def test_article_vote(self):
        article = Article.objects.get(slug='test-article')
        article.upvote()
        self.assertEqual(article.upvotes, 1)

        article.downvote()
        self.assertEqual(article.downvotes, 1)

    def test_comment_creation(self):
        article = Article.objects.get(slug='test-article')
        comment = Comment.objects.create(
            article=article,
            name='John',
            email='john@example.com',
            body='This is a test comment',
            approved=True,
        )
        self.assertEqual(article.comments.count(), 1)
        self.assertEqual(comment.article, article)
        self.assertEqual(comment.name, 'John')
        self.assertEqual(comment.email, 'john@example.com')
        self.assertEqual(comment.body, 'This is a test comment')
        self.assertTrue(comment.approved)