# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .forms import UserRegistrationForm


class CustomUserTest(TestCase):

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1'
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein2'
        })

        self.assertFalse(form.is_valid())