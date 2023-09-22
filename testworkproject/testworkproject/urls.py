from django.contrib import admin
from django.urls import path

from lessons.views import (AllLessonsAPIView,
                           LessonsByProductAPIView,
                           ProductStatisticsAPIView,
                           MyTokenObtainPairView,
                           MyTokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/', AllLessonsAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonsByProductAPIView.as_view(), name='lesson-detail'),
    path('products/stats/', ProductStatisticsAPIView.as_view(), name='product-stats'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
