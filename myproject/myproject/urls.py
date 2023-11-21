from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import StudentViewSet, CourseViewSet, SemesterViewSet, TeacherViewSet, StudentCardViewSet, SemesterCourseViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API docs",
      default_version='v1',
      description="API для учреждения образования.",
      contact=openapi.Contact(url="https://t.me/mrjlist", name='Мой телеграм для связи'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'course', CourseViewSet)
router.register(r'semester', SemesterViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'studentcard', StudentCardViewSet)
router.register(r'semestercourse', SemesterCourseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/docs<format>/', schema_view.without_ui(cache_timeout=0), name='docs-schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs-schema'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
