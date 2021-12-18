from django.db import models
from django.db.models.deletion import DO_NOTHING
# Create your models here.


class DifficultyModel(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    difficulty_name = models.CharField(max_length=30)

    def __str__(self):
        return self.difficulty_name


class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    difficulty_id = models.ForeignKey(
        DifficultyModel, on_delete=models.DO_NOTHING, related_name='difficulty')

    def __str__(self):
        return self.name


class ExerciseModel(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500, null=True)
    audio_url = models.CharField(max_length=500, null=True)
    course_id = models.ForeignKey(
        CourseModel, on_delete=models.CASCADE, related_name='exercises')
