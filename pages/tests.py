from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.res = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.res.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.res, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.res, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
        view.func.__name__,
        HomePageView.as_view().__name__
        )

class TestAboutPage(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.res = self.client.get(url)

    def test_aboutPage_status_code(self):
        self.assertEqual(self.res.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.res, 'about.html')

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.res, 'About Page')

    def test_aboutPage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.res, 'Hi there! I should not be on the page.'
        )
    
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
        view.func.__name__,
        AboutPageView.as_view().__name__
        )