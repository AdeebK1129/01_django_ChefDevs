from django import forms

class RecipeForm(forms.Form):
    food_name = forms.CharField(label='Food Name', max_length=100)