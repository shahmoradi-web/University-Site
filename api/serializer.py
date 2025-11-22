from courses.models import Course
from rest_framework import serializers



class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.first_name', read_only=True)
    class Meta:
        model = Course
        fields = ['id','name','teacher','term','credit']
