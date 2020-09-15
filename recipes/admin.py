from django.contrib import admin
from recipes.models import Tag, Recipe, RecipeIngredient, Follow


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "tag_name")
    search_fields = ("tag_name",)
    empty_value_display = '-пусто-'


admin.site.register(Tag, TagAdmin)
admin.site.register(Follow)

class RecipeAdmin(admin.ModelAdmin):
    raw_id_fields = ("ingredients", "tag", "favourite")
    list_display = ("id", "title")
    search_fields = ("title",)
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity")
    empty_value_display = '-пусто-'


admin.site.register(RecipeIngredient, RecipeIngredientAdmin)