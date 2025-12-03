
from django.test import TestCase,Client
from django.urls import reverse
from accounts.models import CustomUser
from courses.forms import CourseSelectForm
from courses.models import Course
from users.models import StudentProfile



class TestLoginRequired(TestCase):
    def test_all_views_required_login(self):
        protected_urls = [
            reverse('student_portal:dashboard'),
            reverse('student_portal:settings'),
            reverse('student_portal:edit_student_profile'),
            reverse('student_portal:student_add_courses'),
            reverse('student_portal:show_student_courses'),
            reverse('student_portal:show_announcement'),
        ]
        self.client.logout()
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/accounts/login/', response.url)


class TsetDashboardViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
            )

        self.student = StudentProfile.objects.create(
            user = self.user,father_name = 'reza',
            faculty = 'engineering',major = 'software',
            entry_term = '1390'
        )

        self.url = reverse('student_portal:dashboard')

    def test_dashboard_context_data(self):
        self.client.login(username='testuser',
                          password='Password123@#$')
        response = self.client.get(self.url)

        self.assertEqual(response.context['first_name'], 'ali')
        self.assertEqual(response.context['last_name'], 'ahmadi')
        self.assertEqual(response.context['department'], 'cs')
        self.assertEqual(response.context['father_name'], 'reza')
        self.assertEqual(response.context['faculty'],'engineering')
        self.assertEqual(response.context['major'],'software')
        self.assertEqual(response.context['entry_term'],'1390')


class TestEditStudentProfileViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:edit_student_profile')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.student = StudentProfile.objects.create(
            user=self.user, father_name='reza',
            faculty='engineering', major='software',
            entry_term='1390'
        )

    def test_get_request_render(self):
        self.client.login(username='testuser',password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_student_profile.html')
        self.assertIn('form', response.context)

    def test_updates_profile(self):
        self.client.login(username='testuser',password='Password123@#$')
        data = {
            'email': 'ali@gmail.com',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('student_portal:dashboard'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.email, data['email'])

    def test_post_invalid_form(self):
        self.client.login(username='testuser',password='Password123@#$')
        data = {
            'email': 'ali@gmail',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_student_profile.html')
        self.assertTrue(response.context['form'].errors)


class TestStudentAddCourseViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:student_add_courses')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.student = StudentProfile.objects.create(
            user=self.user, father_name='reza',
            faculty='engineering', major='software',
            entry_term='1390',
        )


    def test_get_request_render(self):
        self.client.login(username='testuser',password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_add_courses.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'],CourseSelectForm)

    def test_student_add_course(self):
        self.client.login(username='testuser',
                          password='Password123@#$')

        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        course1 = Course.objects.create(name='math1',
                                        teacher=self.user_teacher, term='5',
                                        credit=3)
        course2 = Course.objects.create(name='math2',
                                        teacher=self.user_teacher, term='5',
                                        credit=3)

        data = {
                'courses':[course1.id, course2.id]
            }
        response = self.client.post(self.url, data)
        self.student.refresh_from_db()

        self.assertRedirects(response, reverse('student_portal:dashboard'))
        self.assertEqual(self.student.courses.count(), 2)
        self.assertIn(course1, self.student.courses.all())
        self.assertIn(course2, self.student.courses.all())
