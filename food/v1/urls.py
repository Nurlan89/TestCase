from django.urls import path
from food.v1.views import FoodListAPIView

urlpatterns = [
    path('foods/', FoodListAPIView.as_view()),
]