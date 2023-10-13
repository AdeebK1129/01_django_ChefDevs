from django.shortcuts import render, redirect
from django.http import HttpResponse
from .recipe_forms import RecipeForm
import datetime
import json

food_recipes = {
    'Beef and Broccoli Stir-Fry': {
        'recipe': """
            1. Slice beef thinly and marinate in soy sauce, garlic, and ginger.
            2. In a wok, stir-fry marinated beef until browned.
            3. Add broccoli florets and sliced bell peppers.
            4. Mix oyster sauce, soy sauce, and sesame oil for the sauce.
            5. Pour the sauce over the beef and veggies, tossing to coat.
            6. Serve the Beef and Broccoli over rice.
            7. Garnish with sesame seeds and green onions.
            8. Enjoy this flavorful stir-fry!
        """,
        'food_name': 'Beef and Broccoli',
        'food_image': 'image/Beef_and_Broccoli_Stir-Fry.jpg'
    },
    'Bibimbap': {
        'recipe': """
            1. Cook short-grain rice and set aside.
            2. Sauté julienned carrots, spinach, mushrooms, and bean sprouts separately.
            3. Season each vegetable with sesame oil and soy sauce.
            4. Fry an egg sunny-side-up.
            5. Arrange rice in a bowl and top with the sautéed vegetables.
            6. Place the fried egg on top.
            7. Add a dollop of gochujang (Korean red pepper paste).
            8. Mix everything together before eating your Bibimbap!
        """,
        'food_name': 'Bibimbap',
        'food_image': 'image/Bibimbap.jpg'
    },
    'Caprese Salad': {
        'recipe': """
            1. Slice fresh tomatoes and mozzarella into 1/4-inch thick slices.
            2. Arrange tomato and mozzarella slices on a serving platter.
            3. Tuck fresh basil leaves between the tomato and mozzarella slices.
            4. Drizzle extra virgin olive oil and balsamic glaze over the salad.
            5. Sprinkle with salt and pepper to taste.
            6. Serve your Caprese Salad immediately for a refreshing dish!
        """,
        'food_name': 'Caprese Salad',
        'food_image': 'image/Caprese_Salad.jpg'
    },
    'Caesar Salad': {
        'recipe': """
            1. Wash and dry Romaine lettuce, then tear into bite-sized pieces.
            2. Prepare croutons by toasting bread cubes with olive oil and garlic.
            3. Grate Parmesan cheese and prepare Caesar dressing.
            4. Toss lettuce with dressing, croutons, and grated Parmesan.
            5. Add freshly ground black pepper and a squeeze of lemon.
            6. Serve your Caesar Salad chilled and enjoy!
        """,
        'food_name': 'Caesar Salad',
        'food_image': 'image/Caesar_Salad.webp'
    },
    'Chicken Alfredo': {
        'recipe': """
            1. Cook fettuccine pasta until al dente.
            2. In a pan, melt butter and sauté minced garlic.
            3. Add sliced chicken breasts and cook until no longer pink.
            4. Pour in heavy cream and Parmesan cheese, stirring until creamy.
            5. Season with salt, pepper, and nutmeg.
            6. Toss the cooked pasta in the Alfredo sauce.
            7. Garnish with parsley and extra Parmesan before serving.
        """,
        'food_name': 'Chicken Alfredo',
        'food_image': 'image/Chicken_Alfredo.jpg'
    },
    'Chicken Curry': {
        'recipe': """
            1. Sauté diced chicken in oil until browned.
            2. Add curry powder, cumin, coriander, and chopped onions.
            3. Stir in coconut milk, diced tomatoes, and chicken broth.
            4. Simmer until the chicken is cooked through and the sauce thickens.
            5. Season with salt and pepper to taste.
            6. Serve the Chicken Curry over rice or with naan bread.
            7. Enjoy the rich flavors of your Chicken Curry!
        """,
        'food_name': 'Chicken Curry',
        'food_image': 'image/Chicken_Curry.jpg'
    },
    'Chicken Fajitas': {
        'recipe': """
            1. Slice chicken breasts into strips and marinate in fajita seasoning.
            2. In a skillet, cook sliced bell peppers and onions until softened.
            3. Remove veggies from the skillet and cook the marinated chicken until done.
            4. Mix veggies and chicken together in the skillet.
            5. Warm tortillas and fill with the chicken and veggie mixture.
            6. Top with salsa, guacamole, and sour cream.
            7. Serve your flavorful Chicken Fajitas!
        """,
        'food_name': 'Chicken Fajitas',
        'food_image': 'image/Chicken_Fajitas.jpg'
    },
    'Chicken Parmesan': {
        'recipe': """
            1. Preheat the oven to 375°F (190°C).
            2. Coat chicken breasts in seasoned breadcrumbs.
            3. In a skillet, heat olive oil and brown the chicken on both sides.
            4. Transfer the chicken to a baking dish and top with marinara sauce and mozzarella.
            5. Bake until the cheese is melted and bubbly.
            6. Cook pasta al dente and serve with the chicken.
            7. Garnish with fresh basil and grated Parmesan.
            8. Enjoy your flavorful Chicken Parmesan!
        """,
        'food_name': 'Chicken Parmesan',
        'food_image': 'image/Chicken_Parmesan.jpg'
    },
    'Chicken Teriyaki': {
        'recipe': """
            1. Marinate chicken thighs in a mixture of soy sauce, sake, and mirin.
            2. In a skillet, cook the marinated chicken until browned.
            3. Pour in the teriyaki sauce (soy sauce, sake, mirin, sugar) to glaze the chicken.
            4. Add sliced green onions for freshness.
            5. Serve the Chicken Teriyaki over steamed rice.
            6. Garnish with sesame seeds and enjoy the savory dish!
        """,
        'food_name': 'Chicken Teriyaki',
        'food_image': 'image/Chicken_Teriyaki.jpg'
    },
    'Chocolate Cake': {
        'recipe': """
            1. Preheat the oven to 350°F (175°C) and grease two cake pans.
            2. In a bowl, mix flour, cocoa powder, baking soda, and salt.
            3. In another bowl, beat butter, sugar, eggs, and vanilla extract.
            4. Gradually add the dry ingredients to the wet ingredients, alternating with milk.
            5. Pour the batter into the prepared pans and bake for 30-35 minutes.
            6. Let the cakes cool, then frost with chocolate icing.
            7. Slice and enjoy your decadent Chocolate Cake!
        """,
        'food_name': 'Chocolate Cake',
        'food_image': 'image/Chocolate_Cake.jpg'
    },
    'Chocolate Chip Cookies': {
        'recipe': """
            1. Preheat the oven to 350°F (175°C).
            2. In a bowl, cream together butter, white sugar, and brown sugar.
            3. Beat in eggs one at a time, then stir in vanilla extract.
            4. In a separate bowl, mix flour, baking soda, and salt.
            5. Combine wet and dry ingredients, then fold in chocolate chips.
            6. Drop rounded tablespoons of dough onto a baking sheet.
            7. Bake for 10-12 minutes or until the edges are golden.
            8. Let the cookies cool on the baking sheet for a few minutes before transferring to a wire rack.
            9. Enjoy warm and gooey Chocolate Chip Cookies!
        """,
        'food_name': 'Chocolate Chip Cookies',
        'food_image': 'image/Chocolate_Chip_Cookies_.jpg'
    },
    'Dim Sum Shumai': {
        'recipe': """
            1. Mix ground shrimp, minced garlic, ginger, and soy sauce.
            2. Place a spoonful of the shrimp mixture in the center of a dumpling wrapper.
            3. Fold the edges of the wrapper towards the center, leaving the top open.
            4. Place the dumplings in a steamer and steam until cooked.
            5. Garnish with chopped green onions.
            6. Serve the Shumai with soy sauce and enjoy your Dim Sum!
        """,
        'food_name': 'Dim Sum Shumai',
        'food_image': 'image/Dim_Sum_Shumai.jpg'
    },
    'Gourmet Macaroni and Cheese': {
        'recipe': """
            1. Cook macaroni until al dente and set aside.
            2. In a saucepan, melt butter and whisk in flour to make a roux.
            3. Gradually add milk, stirring constantly until the sauce thickens.
            4. Add shredded cheddar, gouda, and gruyere cheeses.
            5. Season with mustard, salt, and pepper.
            6. Combine the cheese sauce with cooked macaroni.
            7. Optional: Top with breadcrumbs and bake until golden and bubbly.
            8. Serve your Gourmet Macaroni and Cheese hot and creamy!
        """,
        'food_name': 'Macaroni and Cheese',
        'food_image': 'image/Gourmet_Macaroni_and_Cheese.jpg'
    },
    'Grilled Salmon': {
        'recipe': """
            1. Season salmon fillets with salt, pepper, and a squeeze of lemon.
            2. Preheat the grill to medium-high heat.
            3. Grill salmon for 4-5 minutes per side or until cooked through.
            4. Optional: Brush with a honey glaze for added flavor.
            5. Serve the Grilled Salmon with a side of vegetables or salad.
            6. Enjoy the light and healthy Grilled Salmon!
        """,
        'food_name': 'Grilled Salmon',
        'food_image': 'image/Grilled_Salmon.jpg'
    },
    'Hamburger': {
        'recipe': """
            1. Season ground beef with salt and pepper.
            2. Shape the beef into patties and grill to your desired doneness.
            3. Toast hamburger buns on the grill or in a toaster.
            4. Assemble the burger with lettuce, tomato, onion, and your favorite condiments.
            5. Add cheese if desired and let it melt.
            6. Place the patty on the bun, stack toppings, and enjoy your Hamburger!
        """,
        'food_name': 'Hamburger',
        'food_image': 'image/Hamburger.jpg'
    },
    'Kung Pao Chicken': {
        'recipe': """
            1. Sauté diced chicken in a wok until browned.
            2. Add diced bell peppers, peanuts, and dried red chilies.
            3. In a bowl, mix soy sauce, vinegar, and sugar for the sauce.
            4. Pour the sauce over the chicken and veggies.
            5. Stir-fry until everything is well coated and cooked.
            6. Garnish with chopped green onions and sesame seeds.
            7. Serve your flavorful Kung Pao Chicken over rice.
            8. Enjoy the spicy and tangy taste!
        """,
        'food_name': 'Kung Pao Chicken',
        'food_image': 'image/Kung_Pao_Chicken.jpg'
    },
    'Lemon Garlic Butter Shrimp': {
        'recipe': """
            1. In a skillet, melt butter and sauté minced garlic until fragrant.
            2. Add large shrimp to the skillet and cook until pink.
            3. Squeeze fresh lemon juice over the shrimp.
            4. Season with salt, black pepper, and red pepper flakes.
            5. Stir in chopped parsley for freshness.
            6. Serve the Lemon Garlic Butter Shrimp over pasta or rice.
            7. Enjoy the zesty flavors of this quick dish!
        """,
        'food_name': 'Lemon Garlic Butter Shrimp',
        'food_image': 'image/Lemon_Garlic_Butter_Shrimp.jpg'
    },
    'Macaroni and Cheese': {
        'recipe': """
            1. Cook macaroni until al dente and set aside.
            2. In a saucepan, melt butter and whisk in flour to make a roux.
            3. Gradually add milk, stirring constantly until the sauce thickens.
            4. Add shredded cheddar, gouda, and gruyere cheeses.
            5. Season with mustard, salt, and pepper.
            6. Combine the cheese sauce with cooked macaroni.
            7. Optional: Top with breadcrumbs and bake until golden and bubbly.
            8. Serve your Gourmet Macaroni and Cheese hot and creamy!
        """,
        'food_name': 'Macaroni and Cheese',
        'food_image': 'image/Macaroni_and_Cheese.jpg'
    },
    'Mango Salsa': {
        'recipe': """
            1. Dice ripe mangoes, red onion, and tomatoes.
            2. Finely chop cilantro and jalapeño for a kick.
            3. Mix everything in a bowl and squeeze in lime juice.
            4. Season with salt and pepper to taste.
            5. Optional: Add diced avocado for creaminess.
            6. Let the salsa sit for flavors to meld.
            7. Serve with tortilla chips or as a topping for grilled chicken.
            8. Enjoy the freshness of Mango Salsa!
        """,
        'food_name': 'Mango Salsa',
        'food_image': 'image/Mango_Salsa.jpg'
    },
    'Margherita Pizza': {
        'recipe': """
            1. Preheat the oven to 475°F (245°C).
            2. Roll out pizza dough on a floured surface.
            3. Spread a thin layer of tomato sauce over the dough.
            4. Add slices of fresh mozzarella and cherry tomatoes.
            5. Drizzle with olive oil and sprinkle with fresh basil.
            6. Bake in the oven for 10-12 minutes or until the crust is golden.
            7. Slice and enjoy your Margherita Pizza!
        """,
        'food_name': 'Margherita Pizza',
        'food_image': 'image/Margherita_Pizza.jpg'
    },
    'Pad Thai': {
        'recipe': """
            1. Soak rice noodles in warm water until soft, then drain.
            2. In a wok, heat oil and sauté minced garlic and tofu or shrimp.
            3. Add the soaked noodles to the wok.
            4. Push the noodles to one side and crack an egg into the wok, scramble it, and mix with the noodles.
            5. Add tamarind paste, fish sauce, sugar, and chili powder.
            6. Toss in bean sprouts, green onions, and crushed peanuts.
            7. Stir everything together until well combined.
            8. Serve your Pad Thai with lime wedges and enjoy!
        """,
        'food_name': 'Pad Thai',
        'food_image': 'image/Pad_Thai.jpg'
    },
    'Pizza': {
        'recipe': """
            1. Preheat the oven to 475°F (245°C).
            2. Roll out pizza dough on a floured surface.
            3. Spread a thin layer of tomato sauce over the dough.
            4. Add slices of fresh mozzarella and cherry tomatoes.
            5. Drizzle with olive oil and sprinkle with fresh basil.
            6. Bake in the oven for 10-12 minutes or until the crust is golden.
            7. Slice and enjoy your Margherita Pizza!
        """,
        'food_name': 'Pizza',
        'food_image': 'image/Pizza.jpg'
    },
    'Shrimp Pad See Ew': {
        'recipe': """
            1. Cook wide rice noodles according to package instructions.
            2. In a wok, stir-fry shrimp until pink.
            3. Push shrimp to the side and scramble eggs in the wok.
            4. Add cooked noodles and soy sauce.
            5. Toss in Chinese broccoli or regular broccoli.
            6. Add a splash of fish sauce and stir to combine.
            7. Serve your Shrimp Pad See Ew with lime wedges.
            8. Enjoy this Thai noodle dish!
        """,
        'food_name': 'Shrimp Pad See Ew',
        'food_image': 'image/Shrimp_Pad_See_Ew.jpg'
    }, 
    'Shrimp Scampi': {
        'recipe': """
            1. Cook linguine pasta until al dente and set aside.
            2. In a skillet, sauté minced garlic in olive oil.
            3. Add shrimp and cook until pink.
            4. Deglaze the pan with white wine and chicken broth.
            5. Stir in lemon juice and red pepper flakes.
            6. Toss the cooked pasta with the shrimp and sauce.
            7. Garnish with chopped parsley and grated Parmesan.
            8. Serve your delightful Shrimp Scampi!
        """,
        'food_name': 'Shrimp Scampi',
        'food_image': 'image/Shrimp_Scampi.jpg'
    },
    'Spaghetti Bolognese': {
        'recipe': """
            1. Heat olive oil in a pan and sauté onions and garlic until fragrant.
            2. Add ground beef and cook until browned.
            3. Stir in tomato paste, diced tomatoes, and Italian herbs.
            4. Simmer the sauce for 30-45 minutes to develop flavors.
            5. Cook spaghetti according to package instructions.
            6. Serve the Bolognese sauce over cooked spaghetti.
            7. Garnish with grated Parmesan cheese and fresh basil.
        """,
        'food_name': 'Spaghetti Bolognese',
        'food_image': 'image/Spaghetti_Bolognese.jpg'
    },
    'Spring Rolls': {
        'recipe': """
            1. Soak rice vermicelli noodles in hot water until softened.
            2. Dip rice paper wrappers in warm water to soften.
            3. Place a lettuce leaf on the wrapper and add noodles, shredded carrots, and mint leaves.
            4. Fold the sides of the wrapper and roll tightly.
            5. Mix hoisin sauce with peanut butter for dipping.
            6. Serve your fresh Spring Rolls with the peanut sauce.
            7. Enjoy these light and flavorful rolls!
        """,
        'food_name': 'Spring Rolls',
        'food_image': 'image/Spring_Rolls.jpg'
    },
    'Steak Tacos': {
        'recipe': """
            1. Marinate flank steak in lime juice, cumin, and chili powder.
            2. Grill the steak to your desired doneness and slice thinly.
            3. Warm corn tortillas on the grill or in a pan.
            4. Fill tortillas with sliced steak and top with diced onions and cilantro.
            5. Squeeze fresh lime juice over the tacos.
            6. Optional: Add salsa or guacamole for extra flavor.
            7. Enjoy your flavorful Steak Tacos!
        """,
        'food_name': 'Steak Tacos',
        'food_image': 'image/Steak_Tacos.jpeg'
    },
    'Tiramisu': {
        'recipe': """
            1. Brew strong coffee and let it cool.
            2. In a bowl, whisk egg yolks and sugar until creamy.
            3. Add mascarpone cheese to the egg mixture and mix until smooth.
            4. Dip ladyfingers in the cooled coffee and layer them in a dish.
            5. Spread a layer of the mascarpone mixture over the ladyfingers.
            6. Repeat layers and dust the top with cocoa powder.
            7. Refrigerate the Tiramisu for at least 4 hours.
            8. Slice and enjoy the classic Italian dessert!
        """,
        'food_name': 'Tiramisu',
        'food_image': 'image/Tiramisu.jpg'
    },
    'Tomato Basil Pasta': {
        'recipe': """
            1. Cook your favorite pasta until al dente.
            2. In a pan, sauté minced garlic in olive oil until golden.
            3. Add fresh tomatoes and cook until they start to break down.
            4. Season with salt, black pepper, and a pinch of sugar.
            5. Toss the cooked pasta in the tomato and garlic mixture.
            6. Stir in fresh basil leaves just before serving.
            7. Garnish with grated Parmesan cheese.
            8. Enjoy the simplicity of Tomato Basil Pasta!
        """,
        'food_name': 'Tomato Basil Pasta',
        'food_image': 'image/Tomato_Basil_Pasta.jpg'
    },
    'Vegetable Stir-Fry': {
        'recipe': """
            1. Chop your favorite vegetables (broccoli, bell peppers, carrots, snap peas).
            2. In a wok, stir-fry the vegetables in sesame oil until tender-crisp.
            3. Add soy sauce, ginger, and garlic for flavor.
            4. Optional: Add tofu or your choice of protein.
            5. Toss everything until well combined and heated through.
            6. Serve your Vegetable Stir-Fry over rice or noodles.
            7. Enjoy this quick and healthy dish!
        """,
        'food_name': 'Vegetable Stir-Fry',
        'food_image': 'image/Vegetable_Stir_Fry.jpg'
    }
}

#Index View with Post Form
def index(request):
    json_recipes = json.dumps(food_recipes) #json string convertion
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            food_name = form.cleaned_data['food_name']
            if food_name in food_recipes:
                recipe_details = food_recipes[food_name]
                recipe = recipe_details['recipe']
                return render(request, 'recipes/recipe_info.html', {'food_name': food_name, 'recipe_details': recipe_details, 'recipe': recipe, 'json_recipes': json_recipes})

    else:
        form = RecipeForm()

    return render(request, 'recipes/index.html', {'form': form, 'food_name': None, 'recipe': None, 'food_recipes': food_recipes})

def recipe_info(request):
    json_recipes = json.dumps(food_recipes) #json string convertion
    food_name = request.POST.get('food_name')
    visit_count_key = f'visit_count_{food_name.replace(" ", "_")}' if food_name else 'visit_count_unknown'
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

    if food_name and food_name in food_recipes:
        recipe_details = food_recipes[food_name]
        recipe = recipe_details['recipe']
        image_path = recipe_details.get('food_image', '')  
        response = render(request, 'recipes/recipe_info.html', {'food_name': food_name, 'visit_count': visit_count, 'recipe': recipe, 'image_path': image_path})
        
        response.set_cookie(key=visit_count_key_with_date, value=visit_count, expires=datetime.datetime.combine(current_date + datetime.timedelta(days=1), datetime.time.min))
        return response
    else:
        error_message = f'Sorry, no recipe available for "{food_name}". Try going back and searching for a food from the recipes list.'
        return render(request, 'recipes/recipe_info.html', {'food_name': food_name, 'error_message': error_message, 'visit_count': visit_count, 'recipe': None, 'json_recipes': json_recipes})