from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ('exercise_id', 'name', 'description', 'image_url', 'audio_url', 'course_id')


class CourseSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = ('course_id', 'name', 'description',
                  'difficulty', 'exercises')

    # def create(self, validated_data):
    #     course = CourseModel(name=validated_data.get("name"))
    #     course.save()
    #     # exercises = validated_data.get('tracks')
    #     # for exercise in exercises:
    #     #     ExerciseModel.objects.create(course_id=course, **exercise)
    #     return validated_data
