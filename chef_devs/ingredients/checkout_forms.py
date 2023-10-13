from django import forms

class Checkout(forms.Form):
    ingredient_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search...'}))
