# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from posts.models import Group, Post, Comment
from django.forms import ModelForm
# from django.core.exceptions import ValidationError
from django import forms
from recipes.models import Ingredient, Recipe
from .models import Tag

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "units")

class RecipeForm(ModelForm):
    # tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    # def __init__(self, *args, **kwargs):
    #     # Only in case we build the form from an instance
    #     # (otherwise, 'toppings' list should be empty)
    #     if kwargs.get('instance'):
    #         # We get the 'initial' keyword argument or initialize it
    #         # as a dict if it didn't exist.                
    #         initial = kwargs.setdefault('initial', {})
    #         # The widget for a ModelMultipleChoiceField expects
    #         # a list of primary key for the selected data.
    #         initial['tag'] = [t.pk for t in kwargs['instance'].tag.all()]

    #     forms.ModelForm.__init__(self, *args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     super(RecipeForm, self).__init__(*args, **kwargs)
    #     self.fields['tag'].choices = [(e.id, e.tag_name) for e in Tag.objects.all()]

    class Meta:
        model = Recipe
        fields = ("title", "tag", 'cooking_duration', 'description', 'image')

        # widgets = {
        #     'description': forms.Textarea(),
        #     'tag': forms.CheckboxSelectMultiple()
        # }
    

    

    # def clean_text(self):
    #     cleaned_data = self.cleaned_data['text']
    #     if len(cleaned_data) < 20:
    #         raise forms.ValidationError("Длина поста должна быть более 20 символов!")
    #     return cleaned_data
