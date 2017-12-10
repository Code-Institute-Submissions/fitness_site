# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Product


class ProductPageTest(TestCase):
    def test_check_content_is_correct(self):
        subject_page = self.client.get('/membership/')
        self.assertTemplateUsed(subject_page, "membership.html")
        subject_page_template_output = render_to_response("membership.html",
                                                          {'Product':
                                                               Product.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)

# Create your tests here.
