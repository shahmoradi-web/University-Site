from django.test import TestCase
from accounts.forms import UserRegisterForm
from accounts.models import CustomUser


class TestUserRegisterForm(TestCase):

    def test_exit_email(self):
        CustomUser.objects.create_user(username='testuser', email='testuser@gmail.com', password='Password123!@')
        form = UserRegisterForm(data={'username':'testuser2','first_name':'testuser_first','last_name':'testuser_last','department':'cs','email': 'testuser@gmail.com', 'password1': 'Password123!@','password2': 'Password123!@'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))

    def test_unmached_password(self):
        form = UserRegisterForm(data={'username':'testuser2','first_name':'testuser_first','last_name':'testuser_last','department':'cs','email': 'testuser@gmail.com', 'password1': 'Password123!','password2': 'Password123!@'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error)

