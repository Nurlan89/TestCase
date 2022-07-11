from django.urls import path, include
from food.v1 import urls
urlpatterns = [
    path("v1/", include(('food.v1.urls', 'food'), namespace='v1')),
]