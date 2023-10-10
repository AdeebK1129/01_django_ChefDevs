from django.shortcuts import render
from django.http import HttpResponse
import datetime

food_recipes = {
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
        'food_name': 'Spaghetti'
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
        'food_name': 'Chicken Alfredo'
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
        'food_name': 'Pizza'
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
        'food_name': 'Chocolate Cake'
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
        'food_name': 'Caesar Salad'
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
        'food_name': 'Hamburger'
    },
    'Sushi': {
        'recipe': """
            1. Prepare sushi rice following package instructions.
            2. Lay a sheet of nori on a bamboo sushi mat.
            3. Wet your hands and spread a thin layer of rice on the nori.
            4. Add your favorite sushi ingredients (fish, avocado, cucumber, etc.).
            5. Roll the sushi tightly using the bamboo mat.
            6. Slice the roll into bite-sized pieces.
            7. Serve with soy sauce, pickled ginger, and wasabi.
            8. Enjoy making and eating your homemade Sushi!
        """,
        'food_name': 'Sushi'
    },
    'Tacos': {
        'recipe': """
            1. Season ground beef with taco seasoning and cook until browned.
            2. Warm corn or flour tortillas in a dry skillet.
            3. Assemble tacos with seasoned beef, shredded lettuce, diced tomatoes, and cheese.
            4. Top with salsa, sour cream, and chopped cilantro.
            5. Squeeze lime juice over the tacos before serving.
            6. Enjoy your flavorful and delicious Tacos!
        """,
        'food_name': 'Tacos'
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
        'food_name': 'Chicken Curry'
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
        'food_name': 'Salmon'
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
        'food_name': 'Caprese Salad'
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
        'food_name': 'Chocolate Chip Cookies'
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
        'food_name': 'Pad Thai'
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
        'food_name': 'Macaroni and Cheese'
    },
}
#Index 
def index(request):

#Cookies
def cookies(request):
    dico_cookies = request.COOKIES