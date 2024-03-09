from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Recipe

def home(request, *args, **kwargs):
    HTML_STRING = render_to_string("home.html")
    return HttpResponse(HTML_STRING)
  
# This fuction displays the recipes in the admin data storage.
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('name')
    return render(request, 'recipes.html', {'recipes': recipes})
  
# This function displays the html 'about page'  
def about(request):
    return render(request, "about.html")


# This function in python checks for foods in list then outputs the result
def checkFood(request):
        if request.method == "GET":
           selected_food = request.GET.get("food")
           result = get_diet_info(selected_food)
        else:
           selected_food = ""
           result = ""
        return render(request, "home.html", {"selected_food": selected_food, "result": result})

def get_diet_info(selected_food):
        food_info = {
        "apple": "Apples are low in potassioum, and recomended by the American Kidney Associacion.",
        "banana": "Banana is rich in potassium, eating eat could raise your potassium levels.",
        "chicken": "Chicken can be a good source of protein for most diets, but consider the cooking method and added ingredients.",
        "pizza": "Pizza can be part of a balanced diet, but it's generally high in calories and sodium.",
        "cake": "Cake is typically high in sugar and fat, and is not recommended for regular consumption on most diets.",
        "meat": "Skinless chicken, turkey, fish, and lean beaf are high in potassium, please limit your portion size."
        }
        return food_info.get(selected_food, "Please select a food from the list.")
       
#Eventually I might change the list function to a search bar instead.   
   
"""fruits = ["avocado", "banana", "orange", "prunes", "rasins"]

def search_fruit(request):
  if request.method == "GET":
    fruit_name = request.GET.get("fruit_name")
    
    if fruit_name.lower() in fruits:
      message = f"{fruit_name.capitalize()} is a healthy fruit!"
    else:
      message = f"{fruit_name} is not in the list, but most fruits are generally healthy."
  else:
    fruit_name = ""
    message = f"{fruit_name} is rich in potassium"
  
  return render(request, "home.html", {"fruit_name": fruit_name, "message": message})"""