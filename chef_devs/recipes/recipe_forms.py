from django import forms

class RecipeForm(forms.Form):
    food_name = forms.CharField(label='Enter the food name:')