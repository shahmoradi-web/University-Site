from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import EditTeacherProfileForm
from accounts.models import CustomUser
from users.models import TeacherProfile


# Create your views here.

@login_required
def dashboard(request):
    user = CustomUser.objects.get(id=request.user.id)
    user_teach = TeacherProfile.objects.get(user=user)
    context ={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'department': user.department,
        'teacher_code': user_teach.teacher_code,
    }
    return render(request, 'dashboard.html', context)

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def edit_teacher_profile(request):
    if request.method == 'POST':
        form = EditTeacherProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل به روزرسانی شد',)
            redirect('student_portal:dashboard')
    else:
        form = EditTeacherProfileForm(instance=request.user)
    return render(request, 'edit_student_profile.html', {'form': form})
