from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from accounts.models import CustomUser
from users.models import StudentProfile, TeacherProfile


class TestRegisterStudentsView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:register_students')

    def test_get_request_renders_form(self):
        response = self.client.get(reverse('accounts:register_students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIn('user_form', response.context)
        self.assertIn('student_form', response.context)

    def test_valid_post_creates_user_and_student_form(self):

        data = {
            'username': 'test',
            'password1': 'Password123@#',
            'password2': 'Password123@#',
            'first_name': 'test_first',
            'last_name': 'test_last',

            'major': 'cs',
            'father_name': 'test_father',
            'faculty':'CS',
            'entry_term':'1398'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,reverse('accounts:login_user'))
        user = CustomUser.objects.get(username='test')
        self.assertEqual(user.user_type, 'student')

        student = StudentProfile.objects.get(user=user)
        self.assertEqual(student.major, 'cs')

    def test_register_student_weak_password_should_fail(self):
        data = {
            'username': 'student2',
            'email': 'student2@example.com',
            'password1': '123',
            'password2': '123',
            'first_name': 'Sara',
            'last_name': 'Ahmadi',
            'major': 'CS',
            'father_name': 'Ali',
            'faculty': 'Engineering',
            'entry_term': '1400',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)
        self.assertFalse(CustomUser.objects.filter(username='student2').exists())

    def test_register_student_password_mismatch_should_fail(self):
        data = {
            'username': 'student3',
            'email': 'student3@example.com',
            'password1': 'StrongPass123!',
            'password2': 'Mismatch123!',
            'first_name': 'Mina',
            'last_name': 'Karimi',
            'major': 'CS',
            'father_name': 'Ali',
            'faculty': 'Engineering',
            'entry_term': '1400',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)
        self.assertFalse(CustomUser.objects.filter(username='student3').exists())

    def test_register_student_missing_student_fields_should_fail(self):
        data = {
            'username': 'student4',
            'email': 'student4@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'Reza',
            'last_name': 'Ahmadi',

        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['student_form'].errors)
        self.assertFalse(CustomUser.objects.filter(username='student4').exists())

    def test_register_student_duplicate_username_should_fail(self):
        CustomUser.objects.create_user(username='student5', password='StrongPass123!')
        data = {
            'username': 'student5',
            'email': 'student5@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'Nima',
            'last_name': 'Hosseini',
            'major': 'CS',
            'father_name': 'Ali',
            'faculty': 'Engineering',
            'entry_term': '1400',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)

class TestRegisterTeachersView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:register_teachers')

    def test_get_request_renders_form(self):

        response = self.client.get(reverse('accounts:register_teachers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIn('teacher', response.context)
        self.assertIn('user_form', response.context)

    def test_valid_post_creates_teacher_form(self):

        data = {
            'username': 'test',
            'password1': 'Password123@#',
            'password2': 'Password123@#',
            'first_name': 'test_first',
            'last_name': 'test_last',

        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,reverse('accounts:login_user'))
        user = CustomUser.objects.get(username='test')
        self.assertEqual(user.user_type, 'teacher')
        self.assertTrue(TeacherProfile.objects.filter(user=user).exists())

    def test_invalid_post_show_error(self):
        data = {
            'username': 'teacher2',
            'email': 't2@example.com',
            'password1': '123',
            'password2': '123',
            'first_name': 'Sara',
            'last_name': 'Ahmadi',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)
        self.assertFalse(CustomUser.objects.filter(username='teacher2').exists())

    def test_teacher_register_password_mismatch_should_fail(self):
        data = {
            'username': 'teacher3',
            'email': 't3@example.com',
            'password1': 'StrongPass123!',
            'password2': 'Mismatch123!',
            'first_name': 'Mina',
            'last_name': 'Karimi',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)
        self.assertFalse(CustomUser.objects.filter(username='teacher3').exists())

    def test_teacher_register_duplicate_username_should_fail(self):
        CustomUser.objects.create_user(username='teacher4', password='StrongPass123!')
        data = {
            'username': 'teacher4',
            'email': 't4@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'Nima',
            'last_name': 'Hosseini',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_form'].errors)
