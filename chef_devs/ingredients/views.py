from django.shortcuts import render,redirect
from django.http import HttpResponse
from .checkout import Checkout
import datetime
import json

ingredients = {
    "Avocado": [50, 1.5],
    "Bean sprouts": [30, 0.5],
    "Beef": [60, 6.0],
    "Bell peppers": [40, 0.75],
    "Breadcrumbs": [20, 2.0],
    "Broccoli florets": [45, 1.0],
    "Butter": [70, 2.5],
    "Cabbage": [25, 1.0],
    "Carrots": [80, 0.5],
    "Celery": [35, 0.75],
    "Cheddar cheese": [55, 3.0],
    "Chicken": [70, 5.0],
    "Chili powder": [15, 1.0],
    "Cilantro": [40, 0.25],
    "Cocoa powder": [20, 2.5],
    "Corn tortillas": [30, 1.0],
    "Cumin": [15, 2.0],
    "Curry powder": [20, 2.5],
    "Diced tomatoes": [40, 1.0],
    "Dried red chilies": [10, 3.0],
    "Dumpling wrappers": [50, 2.0],
    "Eggs": [100, 0.3],
    "Extra virgin olive oil": [60, 5.0],
    "Fettuccine pasta": [30, 2.0],
    "Fish sauce": [25, 2.0],
    "Flour": [70, 1.0],
    "Fresh basil": [40, 0.75],
    "Fresh mozzarella": [40, 3.5],
    "Fresh tomatoes": [50, 1.0],
    "Garlic": [90, 0.2],
    "Gochujang": [15, 3.0],
    "Gouda cheese": [35, 4.0],
    "Green onions": [50, 0.25],
    "Ground beef": [60, 5.0],
    "Ground chicken": [55, 4.0],
    "Ground shrimp": [40, 6.0],
    "Honey glaze": [20, 4.0],
    "Italian herbs": [25, 2.0],
    "Jalapeño": [30, 0.5],
    "Lemon": [50, 0.5],
    "Lemon juice": [50, 1.0],
    "Linguine pasta": [30, 2.0],
    "Macaroni": [40, 1.5],
    "Mascarpone cheese": [25, 3.5],
    "Mirin": [30, 4.0],
    "Mushrooms": [40, 2.0],
    "Olive oil": [60, 4.0],
    "Onions": [70, 0.5],
    "Oyster sauce": [25, 3.0],
    "Parmesan cheese": [50, 2.0],
    "Pasta": [60, 2.0],
    "Peanut butter": [30, 2.5],
    "Peanuts": [40, 1.5],
    "Pepper": [80, 0.3],
    "Red chilies": [25, 2.5],
    "Red onion": [35, 0.75],
    "Red pepper flakes": [20, 1.0],
    "Rice": [90, 1.0],
    "Rice noodles": [50, 2.0],
    "Romaine lettuce": [30, 1.0],
    "Sake": [30, 6.0],
    "Salt": [100, 0.2],
    "Sesame oil": [35, 3.0],
    "Sesame seeds": [40, 1.0],
    "Short-grain rice": [60, 2.5],
    "Shrimp": [45, 7.0],
    "Soy sauce": [70, 2.0],
    "Spinach": [50, 1.0],
    "Sugar": [90, 1.0],
    "Tamarind paste": [20, 3.5],
    "Tofu": [45, 2.0],
    "Tomato paste": [30, 1.5],
    "White sugar": [80, 1.0],
    "White wine": [25, 8.0]
}
def index(request):
    if request.method == 'POST':
        form = Checkout(request.POST)
        if form.is_valid():
            ingredient_name = form.cleaned_data['ingredient_name']
            if ingredient_name in ingredients:
                stock = ingredients[ingredient_name][0]
                price = ingredients[ingredient_name][1]
                return render(request, 'ingredients/checkout_info.html', {'ingredient_name': ingredient_name, 'stock': stock, 'price':price})

    else:
        form = Checkout()
    return render(request, 'ingredients/index.html', {'ingredient_name': None, 'stock': None, 'price':None})

def checkout_info(request):
    ingredient_name = request.POST.get('ingredient_name')
    return render(request)
