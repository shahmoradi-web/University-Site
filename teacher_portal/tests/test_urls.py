from django.test import TestCase
from django.urls import reverse, resolve

from teacher_portal.views import *


class TestUrls(TestCase):

    def test_dashboard_url(self):
        url = reverse('teacher_portal:dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_settings_url(self):
        url = reverse('teacher_portal:settings')
        self.assertEqual(resolve(url).func, settings)

    def test_edit_teacher_profile_url(self):
        url = reverse('teacher_portal:edit_teacher_profile')
        self.assertEqual(resolve(url).func, edit_teacher_profile)

    def test_teacher_add_courses_url(self):
        url = reverse('teacher_portal:teacher_add_courses')
        self.assertEqual(resolve(url).func, teacher_add_courses)

    def test_show_courses_url(self):
        url = reverse('teacher_portal:show_courses')
        self.assertEqual(resolve(url).func, show_courses)

    def test_add_announcement_url(self):
        url = reverse('teacher_portal:add_announcement', args=[1])
        self.assertEqual(resolve(url).func, add_announcement)

    def test_show_announcement_url(self):
        url = reverse('teacher_portal:show_announcement', args=[1])
        self.assertEqual(resolve(url).func, show_announcement)


