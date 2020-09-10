from django.contrib import admin
from recipes.models import Tag, Recipe


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "tag_name")
    search_fields = ("tag_name",)
    empty_value_display = '-пусто-'


admin.site.register(Tag, TagAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)