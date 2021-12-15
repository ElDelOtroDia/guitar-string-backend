from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer
