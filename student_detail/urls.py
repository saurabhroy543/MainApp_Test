from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp import views
from mainapp.viewsets import SchoolViewSet, StudentViewSet

routes = DefaultRouter()
routes.register('school', SchoolViewSet, basename='school_v1_API')
routes.register('student', StudentViewSet, basename='student_v1_API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls)),
    path('school-form', views.school_view),
    path('show-school', views.show_school),
    path('edit-school/<int:id>', views.edit_school),
    path('update-school/<int:id>', views.update_school),
    path('delete-school/<int:id>', views.destroy_school),
    path('student-form', views.student_view),
    path('show-student', views.show_student),
    path('edit-student/<int:id>', views.edit_student),
    path('update-student/<int:id>', views.update_student),
    path('delete-student/<int:id>', views.destroy_student),
]
