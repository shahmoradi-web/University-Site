from courses.models import Course
from rest_framework import serializers

from users.models import StudentProfile, TeacherProfile


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.first_name', read_only=True)
    class Meta:
        model = Course
        fields = ['id','name','teacher','term','credit']

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.first_name', read_only=True)
    class Meta:
        model = StudentProfile
        fields = ['id','user','student_id','father_name','faculty',
                  'major','entry_term','grade','courses']


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.first_name', read_only=True)
    class Meta:
        model = TeacherProfile
        fields = ['id','user','teacher_code','courses']