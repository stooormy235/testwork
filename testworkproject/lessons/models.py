from django.db import models
from django.contrib.auth.models import User


# Модель для хранения информации о продукте
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


# Модель для хранения информации об уроке 
class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()


# Модель для хранения информации о просмотре урока пользователями
class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.IntegerField()
    status = models.BooleanField()