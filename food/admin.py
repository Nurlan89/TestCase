from django.contrib import admin
from food.models import Food, FoodCategory
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    pass