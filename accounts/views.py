from http.client import HTTPResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from accounts.forms import *
from datetime import datetime
from users.models import TeacherProfile
# Create your views here.

def home(request):
    pass

def register_students(request):
    student = True
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)

            password = user_form.cleaned_data['password1']
            try:
                validate_password(password, user)  # validate weak password
            except ValidationError as e:
                user_form.add_error('password1', e)

            if user_form.is_valid():
                user.user_type = 'student'
                user.set_password(password)
                user.save()
                student = student_form.save(commit=False)
                student.user = user
                student.save()
                return redirect('accounts:login_user')

    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()

    return render(
        request,
        'registration/register.html',
        {'user_form': user_form,
         'student_form': student_form,
         'student': student}
    )

def register_teachers(request):
    teacher = True

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)

            password = user_form.cleaned_data['password1']
            try:
                validate_password(password, user)  # validate weak password
            except ValidationError as e:
                user_form.add_error('password1', e)

            if user_form.is_valid():
                user.user_type = 'teacher'
                user.set_password(password)
                user.save()
                TeacherProfile.objects.create(user=user)
                return redirect('accounts:login_user')

    else:
        user_form = UserRegisterForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'teacher': teacher
    })
def register_admin(request):
    admin = True
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'admin'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()


            return redirect('login_user')
    else:
        user_form = UserRegisterForm()
    return render(request, 'registration/register.html', {'user_form': user_form,
                                                    'admin': admin})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                now = datetime.now()
                subject = 'ورود به سایت آموزشی'
                message = f'{now.strftime("%Y-%m-%d %H:%M:%S")}ورود به سایت آموزشی\n'
                send_mail(subject, message, 'shahmoradinrges@gmail.com', ['venusshahmoradi3@gmail.com'])

                if user.user_type == 'student':
                    return redirect('student_portal:dashboard')
                elif user.user_type == 'teacher':
                    return redirect('teacher_portal:dashboard')

            else:
                form.add_error(None,'Incorrect username or password.')
    else:
        form = LoginUserForm()
    return render(request,'registration/login_user.html',{'form': form})

def logout_user(request):
    logout(request)
    return redirect('login_user')
