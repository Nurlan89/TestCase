from rest_framework import generics

from food.models import FoodCategory
from food.v1.serializers import FoodListSerializer


class FoodListAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(food__is_publish=True)
    serializer_class = FoodListSerializer


