
from django.test import TestCase,Client
from django.urls import reverse
from accounts.models import CustomUser
from announcement.models import Announcement
from courses.forms import CourseSelectForm
from courses.models import Course, Enrollment
from users.models import StudentProfile



class TestLoginRequired(TestCase):
    def test_all_views_required_login(self):
        protected_urls = [
            reverse('student_portal:dashboard'),
            reverse('student_portal:settings'),
            reverse('student_portal:edit_student_profile'),
            reverse('student_portal:show_student_courses'),
            reverse('student_portal:show_announcement'),
            reverse('student_portal:save_enrollment'),
            reverse('student_portal:take_courses'),
            reverse('student_portal:edit_courses'),
            reverse('student_portal:show_all_courses'),

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



class TestShowAnnouncementViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:show_announcement')
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
        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        self.course = Course.objects.create(name='math1',
                                            teacher=self.user_teacher, term='5',
                                            credit=3)
        self.enrollment = Enrollment.objects.create(course=self.course,user=self.user,teacher=self.user_teacher)
        self.announcement = Announcement.objects.create(course=self.course,teacher=self.user_teacher,
                                                        title='test title',content='test content')

    def test_get_request_render(self):
        self.client.login(username='testuser',password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['announcements']), 1)
        self.assertTemplateUsed(response, 'show_announcement_student.html')


class TestShowAllCoursesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:show_all_courses')
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
        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        self.course = Course.objects.create(name='math1',
                                            teacher=self.user_teacher, term='5',
                                            credit=3)

    def test_get_request_render(self):

        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_all_courses.html')
        self.assertEqual(len(response.context['courses']), 1)


class TestTakeCoursesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:take_courses')
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
        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        self.course = Course.objects.create(id='1', name='math1',capacity='2', register='1',
                                            teacher=self.user_teacher, term='5')

    def test_get_request_render(self):
        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('student_portal:show_student_courses'))

    def test_add_course_student(self):
        self.client.login(username='testuser', password='Password123@#$')
        data = {
            'courses':[self.course.id]
        }
        self.client.post(self.url, data)
        self.student.refresh_from_db()
        self.assertEqual(len(self.student.courses.all()), 1)
        self.assertIn(self.course, self.student.courses.all())

class TestShowStudentCoursesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:show_student_courses')

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
        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_student_courses.html')

class TestSaveEnrollmentViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:save_enrollment')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        self.course = Course.objects.create(id='1', name='math1', capacity='2', register='1',
                                            teacher=self.user_teacher, term='5')

        self.student = StudentProfile.objects.create(
            user=self.user, father_name='reza',
            faculty='engineering', major='software',
            entry_term='1390',
        )
        self.student.courses.add(self.course)

    def test_get_request_render(self):
        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_student_courses.html')

    def test_save_enrollment_not_exists(self):
        self.client.login(username='testuser', password='Password123@#$')
        self.client.get(self.url)
        self.assertEqual(Enrollment.objects.count(), 1)

    def test_save_enrollment_exists(self):
        Enrollment.objects.create(user=self.user, course=self.course,teacher=self.user_teacher,)
        self.client.login(username='testuser', password='Password123@#$')
        self.client.get(self.url)
        self.assertEqual(Enrollment.objects.count(), 1)

    def test_context(self):
        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['courses']), 1)
        self.assertIn(self.course, response.context['courses'])


class TestEditCoursesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student_portal:edit_courses')

        self.user = CustomUser.objects.create_user(
            username='testuser', password='Password123@#$',
            first_name='ali', last_name='ahmadi',
            department='cs',
        )

        self.user_teacher = CustomUser.objects.create_user(
            username='testuser_teacher', password='Password123@#$',
            first_name='abas', last_name='ahmadzade',
            department='cs',
        )

        self.course = Course.objects.create(id='1', name='math1', capacity='2', register='1',
                                            teacher=self.user_teacher, term='5')

        self.student = StudentProfile.objects.create(
            user=self.user, father_name='reza',
            faculty='engineering', major='software',
            entry_term='1390',
        )
        self.student.courses.add(self.course)

    def test_get_request_render(self):
        self.client.login(username='testuser', password='Password123@#$')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_courses.html')
        self.assertIn('courses', response.context)

    def test_remove_courses_student(self):
        self.client.login(username='testuser', password='Password123@#$')
        data = {
            'courses':[self.course.id]
        }
        response = self.client.post(self.url, data)
        self.assertEqual(self.student.courses.count(), 0)
        self.assertEqual(response.status_code, 302)


