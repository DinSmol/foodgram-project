from rest_framework import serializers
from rest_framework.utils import html, model_meta, representation
import traceback
from rest_framework.serializers import raise_errors_on_nested_writes
from collections import OrderedDict
from rest_framework.exceptions import ErrorDetail, ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.fields import (  # NOQA # isort:skip
    CreateOnlyDefault, CurrentUserDefault, SkipField, empty
)
from rest_framework.fields import get_error_detail, set_value

from .models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'units']
