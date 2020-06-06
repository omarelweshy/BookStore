from django.test import TestCase, Client
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='reviewuser',
        email='reviewuser@email.com',
        password='testpass123'
        )
        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
        title='Harry Potter',
        author='JK Rowling',
        price='25.00',
        )

        self.review = Review.objects.create(
        book = self.book,
        author = self.user,
        review = 'An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        res = self.client.get(reverse('book_list'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Harry Potter')
        self.assertTemplateUsed(res, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        res = self.client.get(reverse('book_list'))
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(
        res, '%s?next=/books/' % (reverse('account_login')))
        res = self.client.get(
        '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(res, 'Log In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        res = self.client.get(self.book.get_absolute_url())
        no_res = self.client.get('/books/12345/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(res, 'Harry Potter')
        self.assertContains(res, 'An excellent review')
        self.assertTemplateUsed(res, 'books/book_detail.html')