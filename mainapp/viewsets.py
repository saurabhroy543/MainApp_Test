from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer, SchoolSerializer, StudentBasicSerializer
from .models import School, Student


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=['GET'], detail=False)
    def all_student_data(self, request):
        school = self.request.query_params.get('school')
        if not school:
            return Response({
                'Status': '402:Insufficient Data',
                'detail': "Please provide School Id"})
        school_data = School.objects.filter(id=school).first()
        queryset = Student.objects.filter(school=school)
        data = {
            'School_data': SchoolSerializer(school_data).data,
            'Student_data': StudentBasicSerializer(queryset, many=True).data
        }
        return Response({
            'status': '200',
            'message': "student of th given School are given below",
            'data': data
        })

    @action(methods=['POST'], detail=False)
    def add_student(self, request):
        enrollment = Student.objects.filter(enrollment=request.data.get('enrollment')).first()
        if enrollment:
            return Response({
                'Status': '409:Duplicate data exist',
                'detail': "Please provide Unique Enrollment Number"})
        serializer = StudentSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        update_object = serializer.save()
        data = StudentSerializer(instance=update_object).data

        return Response({
            'status': '200',
            'message': "student Added",
            'data': data
        })

    @action(methods=['GET'], detail=False)
    def all_student(self,request):
        queryset = Student.objects.all()
        data = {
            'Student_data': StudentBasicSerializer(queryset, many=True).data
        }
        return Response({
            'status': '200',
            'message': "GET API for all Student",
            'data': data
        })




class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(methods=['GET'], detail=False)
    def all_school(self,request):
        queryset = School.objects.all()
        data = {
            'School_data': SchoolSerializer(queryset, many=True).data
        }
        return Response({
            'status': '200',
            'message': "GET API for all School",
            'data': data
        })
