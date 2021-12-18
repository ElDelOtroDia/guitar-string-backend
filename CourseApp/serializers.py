from rest_framework import serializers
from .models import *


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # data = data.order_by('-exercise_id').first()
        data = data.order_by('-exercise_id')[:1]
        return super(FilteredListSerializer, self).to_representation(data)


class LastExerciseSerializer (serializers.ModelSerializer):
    class Meta:
        list_serializer_class = FilteredListSerializer
        model = ExerciseModel
        fields = ('exercise_id', 'name')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = ('exercise_id', 'name', 'description',
                  'image_url', 'audio_url', 'course_id')


class CourseSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    # exercises = LastExerciseSerializer(many=True, read_only=True)
    difficulty = serializers.ReadOnlyField(
        source="difficulty_id.difficulty_name")

    class Meta:
        model = CourseModel
        fields = ('course_id', 'name', 'description',
                  'exercises', 'difficulty_id', 'difficulty')


class DifficultySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = DifficultyModel
        fields = ('difficulty_name', 'courses')
