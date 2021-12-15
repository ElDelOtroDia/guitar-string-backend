from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'course', CourseViewSet)
router.register(r'exercise', ExerciseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
