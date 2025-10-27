from Tools.scripts.make_ctype import method
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import *

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
            user.user_type = 'student'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return redirect('login')

    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()

    return render(
        request,
        'register/register.html',
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
            user.user_type = 'teacher'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            TeacherProfile.objects.create(user=user)


            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request,'register/register.html',{'user_form': user_form,
                                                    'teacher': teacher})


def register_admin(request):
    admin = True
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'admin'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()


            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request,'register/register.html',{'user_form': user_form,
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
                return redirect('home')
                # if request.user.user_type == 'student':
                #     return redirect('panel_students')
                # elif request.user.user_type == 'teacher':
                #     return redirect('panel_teachers')
            else:
                form.add_error(None,'Incorrect username or password.')
    else:
        form = LoginUserForm()
    return render(request,'register/login_user.html',{'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
