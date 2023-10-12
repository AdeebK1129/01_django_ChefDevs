from django import forms

class Checkout(forms.Form):
    ingredient_name = forms.CharField(label='Ingredient Name', max_length=100)
