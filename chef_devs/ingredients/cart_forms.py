from django import forms

class CartForm(forms.Form):
    ingredient_name = forms.CharField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, label='Quantity to Buy')
    view = forms.BooleanField(widget=forms.HiddenInput(), required=False)
