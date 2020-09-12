# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from posts.models import Group, Post, Comment
from django.forms import ModelForm
# from django.core.exceptions import ValidationError
from django import forms
from recipes.models import Ingredient

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "units")
    
    # def clean_text(self):
    #     cleaned_data = self.cleaned_data['text']
    #     if len(cleaned_data) < 20:
    #         raise forms.ValidationError("Длина поста должна быть более 20 символов!")
    #     return cleaned_data