from rest_framework.serializers import ModelSerializer

from .models import Student, School


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class StudentBasicSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
