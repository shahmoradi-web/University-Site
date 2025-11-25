from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from accounts.models import CustomUser
from users.models import StudentProfile


class TestRegisterStudentsView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_request_renders_form(self):
        response = self.client.get(reverse('accounts:register_students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIn('user_form', response.context)
        self.assertIn('student_form', response.context)

    def test_valid_post_creates_user_and_student_form(self):
        url = reverse('accounts:register_students')
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
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,reverse('accounts:login_user'))
        user = CustomUser.objects.get(username='test')
        self.assertEqual(user.user_type, 'student')

        student = StudentProfile.objects.get(user=user)
        self.assertEqual(student.major, 'cs')

    def test_invalid_post_show_error(self):
        url = reverse('accounts:register_students')
        data = {
            'username': 'test',
            'password1': '123',
            'password2': '123',
            'first_name': 'test_first',
            'last_name': 'test_last',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertFalse(CustomUser.objects.filter(username='test').exists())
        self.assertContains(response, 'error')

