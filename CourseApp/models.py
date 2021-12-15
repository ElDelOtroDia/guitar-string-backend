from django.db import models
# Create your models here.


class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    difficulty = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ExerciseModel(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    audio_url = models.CharField(max_length=500)
    course_id = models.ForeignKey(
        CourseModel, on_delete=models.CASCADE, related_name='exercises')
