from django.test import TestCase
from django.urls import reverse,resolve

from student_portal.views import *


class TestUrls(TestCase):

    def test_dashboard_urls(self):
        url = reverse('student_portal:dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_settings_urls(self):
        url = reverse('student_portal:settings')
        self.assertEqual(resolve(url).func, settings)

    def test_edit_student_profile_urls(self):
        url = reverse('student_portal:edit_student_profile')
        self.assertEqual(resolve(url).func, edit_student_profile)

    def test_student_add_courses_urls(self):
        url = reverse('student_portal:student_add_courses')
        self.assertEqual(resolve(url).func, student_add_courses)

    def test_show_student_courses_urls(self):
        url = reverse('student_portal:show_student_courses')
        self.assertEqual(resolve(url).func, show_student_courses)

    def test_show_announcement_urls(self):
        url = reverse('student_portal:show_announcement')
        self.assertEqual(resolve(url).func, show_announcement)


