from django.shortcuts import render, redirect

# Create your views here.


def index(request):
   print("You are looking at recipes")
   title_page = "Recipes"
   recipe_list = [
         {
               "Name": "Wonton Soup", 
               "Origin": "China",
               "Ingredients": "X",
               "Time to Cook": "X",
          },
          ]
   
   return render(request, "recipes/index.html",
                  context={'title_page':title_page,
                           'recipe_list':recipe_list})
