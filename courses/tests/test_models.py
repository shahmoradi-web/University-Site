from django.test import TestCase
from model_bakery import baker

from accounts.models import CustomUser
from courses.models import Course, Enrollment


class TestCourseModels(TestCase):

    def test_str_method(self):
        course = baker.make(Course, name='math')
        self.assertEqual(str(course), 'math')


class TestEnrollmentModels(TestCase):

    def test_str_method(self):
        course = baker.make(Course, name='math')
        user = baker.make(CustomUser, username='ali')
        enrollment = baker.make(Enrollment, course=course, user=user, grade=10)
        self.assertEqual(str(enrollment), 'ali - math - 10')