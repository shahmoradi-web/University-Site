from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import StudentProfile
from accounts.models import CustomUser
from announcement.models import Announcement
from courses.models import Enrollment
from accounts.forms import EditStudentProfileForm

# Create your views here.


@login_required
def dashboard(request):
    user = CustomUser.objects.get(id=request.user.id)
    user_st = StudentProfile.objects.get(user=user)
    context ={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'department': user.department,
        'father_name': user_st.father_name,
        'student_id': user_st.student_id,
        'faculty': user_st.faculty,
        'major': user_st.major,
        'entry_term': user_st.entry_term,

    }
    return render(request, 'dashboard.html', context)

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
            redirect('student_portal:dashboard')
    else:
        form = EditStudentProfileForm(instance=request.user)
    return render(request, 'edit_student_profile.html', {'form': form})





