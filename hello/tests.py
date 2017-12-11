# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from hello.views import get_index, about
from django.core.urlresolvers import resolve

class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)


class AboutPageTest(TestCase):
    def test_about_page_resolves(self):
        about_page = resolve('/about')
        self.assertEqual(about_page.func, about)

