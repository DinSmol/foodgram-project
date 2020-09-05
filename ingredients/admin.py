from django.contrib import admin
from ingredients.models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    empty_value_display = '-пусто-'


admin.site.register(Ingredient, IngredientAdmin)
