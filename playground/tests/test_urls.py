from django.test import SimpleTestCase
from django.urls import reverse, resolve

from playground.views import home, about, booking, cars, contact, category, help
from playground.views import home



class TestUrls(SimpleTestCase):

    def test_home_joy_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, home)
    def test_about_joy_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, about)
    def test_booking_joy_url_is_resolved(self):
        url = reverse('booking')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, booking)
    def test_cars_joy_url_is_resolved(self):
        url = reverse('cars')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, cars)
    def test_contact_joy_url_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, contact)
    def test_category_joy_url_is_resolved(self):
        url = reverse('category')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, category)
    def test_help_joy_url_is_resolved(self):
        url = reverse('Help')
        print(resolve(url))
        ##self.assertEquals(resolve(url).func, home)
        self.assertEqual(resolve(url).func, help)

