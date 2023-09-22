from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Lesson, LessonView
from .serializers import ProductSerializer, LessonSerializer, LessonViewSerializer


# Вывод списка всех уроков по продуктам, к которым пользователь имеет доступ
class AllLessonsAPIView(APIView):
    def get(self, request):
        user = request.user
        lessons = Lesson.objects.filter(products__owner=user)
        serializer = LessonSerializer(lessons, many=True, context={'user': user})
        return Response(serializer.data)


# Вывод информации о конкретном уроке, к которому пользователь имеет доступ
class LessonsByProductAPIView(APIView):
    def get(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id, owner=user)
        lessons = product.lesson_set.all()
        serializer = LessonSerializer(lessons, many=True, context={'user': user})
        return Response(serializer.data)

# Вывод статистики по продуктам
class ProductStatisticsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    pass


class MyTokenRefreshView(TokenRefreshView):
    pass