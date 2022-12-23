from django import forms

from mainapp.models import School, Student


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
