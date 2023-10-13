from django import forms

class RecipeForm(forms.Form):
    food_name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Food Name'}))




