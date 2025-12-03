from importlib.resources import contents

from django.test import TestCase,Client
from django.urls import reverse
from psycopg2 import connect

from accounts.forms import EditTeacherProfileForm
from accounts.models import CustomUser
from announcement.forms import AnnouncementForm
from announcement.models import Announcement
from courses.forms import CourseCreateForm
from courses.models import Course
from users.models import TeacherProfile


class TestLoginRequired(TestCase):
    def test_all_views_required_login(self):

        protected_urls = [
            reverse('teacher_portal:dashboard'),
            reverse('teacher_portal:settings'),
            reverse('teacher_portal:edit_teacher_profile'),
            reverse('teacher_portal:teacher_add_courses'),
            reverse('teacher_portal:show_courses'),
            reverse('teacher_portal:add_announcement', args=[1]),
            reverse('teacher_portal:show_announcement', args=[1]),

        ]
        self.client.logout()
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/accounts/login/', response.url)


class TestDashboardView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('teacher_portal:dashboard')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.teacher = TeacherProfile.objects.create(
            user=self.user,
        )

    def test_dashboard_context_data(self):
        self.client.login(username='testuser',
                          password='Password123@#$')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard_teacher.html')
        self.assertEqual(response.context['first_name'], 'ali')
        self.assertEqual(response.context['last_name'], 'ahmadi')
        self.assertEqual(response.context['department'], 'cs')


class TestEditTeacherProfileView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('teacher_portal:edit_teacher_profile')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.teacher = TeacherProfile.objects.create(
            user=self.user,
        )

    def test_get_request_render(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_student_profile.html')
        self.assertIsInstance(response.context['form'], EditTeacherProfileForm)

    def test_update_teacher_profile(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        data={
            'email': 'ali@gmail.com',
        }
        response = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertRedirects(response, reverse('teacher_portal:dashboard'))
        self.assertEqual(self.user.email, data['email'])

class TestTeacherAddCoursesView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('teacher_portal:teacher_add_courses')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.teacher = TeacherProfile.objects.create(
            user=self.user,
        )
    def test_get_request_render(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_add_courses.html')
        self.assertIsInstance(response.context['form'], CourseCreateForm)

    def test_add_courses(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        data = {
            'name':'math',
            'term':'2',
            'credit': 5

        }
        self.client.post(self.url, data)
        self.assertEqual(Course.objects.count(), 1)

    def test_teacher_add_courses(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        data = {
            'name': 'math',
            'term': '2',
            'credit': 5

        }
        self.client.post(self.url, data)
        self.teacher.refresh_from_db()

        self.assertEqual(self.teacher.courses.count(),1)

class TestAddAnnouncementViews(TestCase):

    def setUp(self):
        self.client = Client()


        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.teacher = TeacherProfile.objects.create(
            user=self.user,
        )

        self.course = Course.objects.create(

            name='math',
            teacher=self.user,
            term = '2',
            credit=4
        )


    def test_get_request_render(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        self.url = reverse('teacher_portal:add_announcement', args=[self.course.id])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_announcement_teacher.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], AnnouncementForm)

    def test_add_announcement(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        data = {
            'title':'practise',
            'content':'do practise'
        }
        self.url = reverse('teacher_portal:add_announcement', args=[self.course.id])
        self.client.post(self.url, data)
        self.assertEqual(Announcement.objects.count(), 1)

    def test_add_announcement_invalid_id(self):
        self.url = reverse('teacher_portal:add_announcement', args=[999])
        self.client.login(username='testuser',
                          password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)




