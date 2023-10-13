from django.shortcuts import render,redirect
from django.http import HttpResponse
from .checkout_forms import Checkout
from .cart_forms import CartForm
from django.http import Http404
import datetime
import json

cart_items = {}

ingredients = {
    "Asparagus": [35, 1.25],
    "Avocado": [50, 1.5],
    "Bean sprouts": [30, 0.5],
    "Beef": [60, 6.0],
    "Bell peppers": [40, 0.75],
    "Blueberries": [40, 3.75],
    "Breadcrumbs": [20, 2.0],
    "Broccoli florets": [45, 1.0],
    "Butter": [70, 2.5],
    "Cabbage": [25, 1.0],
    "Carrots": [80, 0.5],
    "Cauliflower": [30, 1.5],
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
    "Grapes": [55, 2.0],
    "Garlic": [90, 0.2],
    "Gochujang": [15, 3.0],
    "Gouda cheese": [35, 4.0],
    "Green onions": [50, 0.25],
    "Ground beef": [60, 5.0],
    "Ground chicken": [55, 4.0],
    "Ground shrimp": [40, 6.0],
    "Honey glaze": [20, 4.0],
    "Italian herbs": [25, 2.0],
    "Jalapeno": [30, 0.5],
    "Kale": [25, 1.0],
    "Lemon": [50, 0.5],
    "Lemon juice": [50, 1.0],
    "Lentils": [50, 2.25],
    "Linguine pasta": [30, 2.0],
    "Macaroni": [40, 1.5],
    "Mango": [45, 1.75],
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
    "Pineapple": [40, 2.5],
    "Quinoa": [60, 3.0],
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
    "White wine": [25, 8.0],
}

def index(request):
    num_tables = 5
    ingredients_per_table = 14

    ingredient_groups = [list(ingredients.items())[i:i + ingredients_per_table] for i in range(0, len(ingredients), ingredients_per_table)]

    if request.method == 'POST':
        form = Checkout(request.POST)
        if form.is_valid():
            ingredient_name = form.cleaned_data['ingredient_name']
            if ingredient_name in ingredients:
                stock = ingredients[ingredient_name][0]
                price = ingredients[ingredient_name][1]
                return render(request, 'ingredients/checkout_info.html', {
                    'ingredient_name': ingredient_name,
                    'stock': stock,
                    'price': price,
                    'ingredients': ingredients,
                    'form': CartForm()  
                })

    else:
        form = Checkout()

    return render(request, 'ingredients/index.html', {'ingredient_groups': ingredient_groups, 'form': form})


def checkout_info(request):
    ingredient_name = request.POST.get('ingredient_name')
    visit_count_key = f'visit_count_{ingredient_name.replace(" ", "_")}' if ingredient_name else 'visit_count_unknown'
    visit_count = 0
    current_date = datetime.datetime.now().date()
    visit_count_key_with_date = f'{visit_count_key}_{current_date}'

    if visit_count_key_with_date in request.COOKIES:
        try:
            visit_count = int(request.COOKIES[visit_count_key_with_date]) + 1
        except ValueError:
            visit_count = 1
    else:
        visit_count = 1

    if ingredient_name in ingredients:
        stock = ingredients[ingredient_name][0]
        price = ingredients[ingredient_name][1]
        max_quantity = stock 
        form = CartForm(initial={'ingredient_name': ingredient_name, 'quantity': 1, 'view': False})
        form.fields['quantity'].widget.attrs['max'] = max_quantity  

        response = render(request, 'ingredients/checkout_info.html', {
            'ingredient_name': ingredient_name,
            'stock': stock,
            'price': price,
            'visit_count': visit_count,
            'form': form 
        })

        response.set_cookie(key=visit_count_key_with_date, value=visit_count,
                            expires=datetime.datetime.combine(current_date + datetime.timedelta(days=1),
                                                             datetime.time.min))
        return response
    else:
        stock = None
        price = None
        error_message = "Ingredient not found"
        form = CartForm()  
        return render(request, 'ingredients/checkout_info.html', {
            'ingredient_name': ingredient_name,
            'error_message': error_message,
            'visit_count': visit_count,
            'stock': stock,
            'price': price,
            'ingredients': ingredients,
            'form': form 
        })



def cart(request):
    view_only = request.POST.get('view') == 'true'
    error_message = None

    if view_only:
        ingredient_name = "Asparagus"
        quantity = 0
        form = CartForm(initial={'ingredient_name': ingredient_name, 'quantity': quantity})
    else:
        if request.method == 'POST':
            form = CartForm(request.POST)
            if form.is_valid():
                ingredient_name = form.cleaned_data['ingredient_name']
                quantity = form.cleaned_data['quantity']

                if ingredient_name in ingredients:
                    stock = ingredients[ingredient_name][0]

                    if quantity <= stock:
                        ingredients[ingredient_name][0] -= quantity

                        if ingredient_name in cart_items:
                            cart_items[ingredient_name]['quantity'] += quantity
                        else:
                            cart_items[ingredient_name] = {
                                'quantity': quantity,
                                'total_price': quantity * ingredients[ingredient_name][1]
                            }

                        total_cost = sum(item['total_price'] for item in cart_items.values())

                        # Ensure total_cost is never negative
                        total_cost = max(total_cost, 0)

                        return render(request, 'ingredients/cart.html', {
                            'cart_items': cart_items,
                            'ingredients': ingredients,
                            'form': CartForm(),
                            'total_cost': total_cost 
                        })
                    else:
                        error_message = f"Insufficient stock. Available: {stock}"
                else:
                    error_message = "Ingredient not found"
            else:
                error_message = "Invalid input"
        else:
            form = CartForm()

    total_cost = sum(item['total_price'] for item in cart_items.values())

    # Ensure total_cost is never negative
    total_cost = max(total_cost, 0)

    return render(request, 'ingredients/cart.html', {
        'form': form,
        'ingredients': ingredients,
        'cart_items': cart_items,
        'error_message': error_message,
        'total_cost': total_cost  # Add total_cost here
    })
    
    
def clear_cart(request):
    cart_items.clear()
    return render (request, 'ingredients/cart.html',)


