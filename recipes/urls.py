from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('<int:id>', views.recipe_detail, name='recipe_detail'),
    path('<int:id>/edit', views.recipe_change, name='recipe_change'),
    path('<int:id>/terminate', views.recipe_delete, name='recipe_delete'),
]
