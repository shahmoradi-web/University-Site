from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from courses.forms import CourseSelectForm
from users.models import StudentProfile
from accounts.models import CustomUser
from announcement.models import Announcement
from courses.models import Enrollment, Course
from accounts.forms import EditStudentProfileForm

# Create your views here.


@login_required
def dashboard(request):
    user = CustomUser.objects.get(id=request.user.id)
    user_st = StudentProfile.objects.get(user=user)
    context ={
        'student':user_st,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'department': user.department,
        'father_name': user_st.father_name,
        'student_id': user_st.student_id,
        'faculty': user_st.faculty,
        'major': user_st.major,
        'entry_term': user_st.entry_term,

    }
    return render(request, 'dashboard_student.html', context)

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def edit_student_profile(request):
    if request.method == 'POST':
        form = EditStudentProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل به روزرسانی شد',)
            return redirect('student_portal:dashboard')
    else:
        form = EditStudentProfileForm(instance=request.user)
    return render(request, 'edit_student_profile.html', {'form': form})


@login_required
def show_announcement(request):
    course_ids = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)
    announcements = Announcement.objects.filter(course_id__in=course_ids)
    return render(request,'show_announcement_student.html', {'announcements': announcements})


@login_required
def show_all_courses(request):
    courses = Course.objects.all()
    return render(request,'show_all_courses.html',{'courses':courses})

@login_required
def take_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    courses = request.POST.getlist('courses')

    for obj in courses:
        course = Course.objects.get(id=int(obj))
        if course.capacity != course.register:
            student.courses.add(course)

    return redirect('student_portal:show_student_courses')


@login_required
def show_student_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    return render(request, 'show_student_courses.html', {'courses': student.courses.all()})


@login_required
def save_enrollment(request):
    student = StudentProfile.objects.get(user=request.user)
    courses = student.courses.all()
    for course in courses:
        if not (Enrollment.objects.filter(course__id=course.id).exists()):
            Enrollment.objects.create(user=request.user, course=course, teacher=course.teacher)
    messages.success(request, 'ثبت نهایی انجام شد', )

    return render(request, 'show_student_courses.html',{'courses':courses})


@login_required
def edit_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        delete_courses = request.POST.getlist('courses')
        student.courses.remove(*delete_courses)
        return redirect('student_portal:show_student_courses')

    return render(request, 'edit_courses.html',{'courses':student.courses.all()})

