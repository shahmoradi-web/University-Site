from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView, \
                                       PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import reverse, resolve
from django.test import TestCase
from accounts.views import *

class TestUrls(TestCase):
    def test_home(self):
        url = reverse('accounts:home')
        self.assertEqual(resolve(url).func, home)

    def test_register_students(self):
        url = reverse('accounts:register_students')
        self.assertEqual(resolve(url).func, register_students)

    def test_register_teachers(self):
        url = reverse('accounts:register_teachers')
        self.assertEqual(resolve(url).func, register_teachers)

    def test_register_admin(self):
        url = reverse('accounts:register_admin')
        self.assertEqual(resolve(url).func, register_admin)

    def test_login_user(self):
        url = reverse('accounts:login_user')
        self.assertEqual(resolve(url).func, login_user)

    def test_logout_user(self):
        url = reverse('accounts:logout_user')
        self.assertEqual(resolve(url).func, logout_user)

    def test_password_change(self):
        url = reverse('accounts:password_change')
        self.assertEqual(resolve(url).func.view_class, PasswordChangeView)

    def test_password_change_done(self):
        url = reverse('accounts:password_change_done')
        self.assertEqual(resolve(url).func.view_class, PasswordChangeDoneView)

    def test_password_reset(self):
        url = reverse('accounts:password_reset')
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done(self):
        url = reverse('accounts:password_reset_done')
        self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_confirm(self):
        uid = 'MQ'
        token = 'set-password-token'
        url = reverse('accounts:password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token,
        })
        self.assertEqual(url, f'/accounts/password_reset/{uid}/{token}/')
    def test_password_reset_complete(self):
        url = reverse('accounts:password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, PasswordResetCompleteView)
