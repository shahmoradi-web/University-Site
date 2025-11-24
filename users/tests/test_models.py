from django.test import TestCase
from users.models import *
from model_bakery import baker
from users.models import *


class TestStudentProfileModel(TestCase):
    def setUp(self):
        self.user = baker.make(CustomUser,username='narges')
        self.student = baker.make(StudentProfile, user = self.user, student_id = 1244)

    def test_model_str(self):
        self.assertEqual(str(self.student), 'narges => 1244')


class TestTeacherProfileModel(TestCase):
    def setUp(self):
        self.user = baker.make(CustomUser,username='ali')
        self.teacher = baker.make(TeacherProfile, user = self.user, teacher_code= 3456)

    def test_model_str(self):
        self.assertEqual(str(self.teacher), 'ali => 3456')
